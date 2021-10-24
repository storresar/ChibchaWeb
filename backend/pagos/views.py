from rest_framework import viewsets
from .models import facturacion,plan
from .serializers import facturacion_serializer
from rest_framework.response import Response
from datetime import datetime,timedelta,date
from django.shortcuts import get_object_or_404
from usuarios.models import cliente,usuario
from auditoria.models import auditoria
from django.core.mail import send_mail
from rest_framework import status

# Create your views here.
class facturacion_viewset(viewsets.ModelViewSet):
    queryset = facturacion.objects.all()
    serializer_class = facturacion_serializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if( instance.fecha_cancelacion <= date.today()):
            actualizacion_pago = facturacion(
                pk = instance.id,
                valor_total = instance.valor_total,
                dominios_disponibles = instance.dominios_disponibles,
                fecha_facturacion = instance.fecha_facturacion,
                fecha_cancelacion = instance.fecha_cancelacion,
                esta_activo = False,
                cod_cliente = instance.cod_cliente,
                cod_plan = instance.cod_plan
            )
            actualizacion_pago.save()
        else:
            print('NO PA')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        request.data._mutable = True
        plan_escogido = get_object_or_404(plan.objects.filter(pk = request.data['cod_plan']))
        periodo =  plan_escogido.periodo_fact
        cliente_Escogido = get_object_or_404(cliente.objects.filter(pk = request.data['cod_cliente']))
        cod_cliente = cliente_Escogido.cod_usuario
        print(cliente_Escogido.has_plan)
        request.data['fecha_facturacion'] = date.today()
        if cliente_Escogido.has_plan == False:
            correo = get_object_or_404(usuario.objects.filter(username = cod_cliente)).email
            if(periodo == 'MENSUAL'):
                print(datetime.now() + timedelta(days=30))
                request.data['fecha_cancelacion'] = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
            elif(periodo == 'ANUAL'):
                print(datetime.now() + timedelta(days=365))
                request.data['fecha_cancelacion'] = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
            request.data['valor_total'] = plan_escogido.valor_plan
            request.data['dominios_disponibles'] = plan_escogido.cant_dominios
            serializer = self.get_serializer(data=request.data)
            if(serializer.is_valid):

                mensaje = '¡GRACIAS! Por suscribirse a un plan a continuacion le regalaremos los detalles de la compra.\n'
                mensaje += '\nNombre del plan:  ' + plan_escogido.nom_plan + '\n'
                mensaje += '\nFecha Facturación:  ' + datetime.now().strftime("%Y-%m-%d") + '\n'
                mensaje += '\nFecha Cancelación:  ' + request.data['fecha_cancelacion'] + '\n'
                send_mail(subject='FACTURACIÓN EXITOSA',message=mensaje,from_email=None,recipient_list=[correo])
                cliente_cambio = cliente(
                    pk = request.data['cod_cliente'],
                    cod_usuario = cliente_Escogido.cod_usuario,
                    has_plan = True
                )
                cliente_cambio.save()
                nueva_auditoria = auditoria(
                    tipo = 'Facturación agregada', 
                    ip=request.META.get('REMOTE_ADDR'),
                    usuario_realiza=cod_cliente,
                    area_afectada = 'FACTURACIÓN'
                )
                nueva_auditoria.save()
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            request.data._mutable = False
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
            request.data._mutable = True
            partial = kwargs.pop('partial', False)
            plan_escogido = get_object_or_404(plan.objects.filter(pk = request.data['cod_plan']))
            periodo =  plan_escogido.periodo_fact
            cliente_Escogido = get_object_or_404(cliente.objects.filter(pk = request.data['cod_cliente']))
            cod_cliente = cliente_Escogido.cod_usuario
            print(cliente_Escogido.has_plan)
            request.data['fecha_facturacion'] = date.today()
            if cliente_Escogido.has_plan == False:
                correo = get_object_or_404(usuario.objects.filter(username = cod_cliente)).email
                if(periodo == 'MENSUAL'):
                    print(datetime.now() + timedelta(days=30))
                    request.data['fecha_cancelacion'] = (datetime.now() + timedelta(days=30)).strftime("%Y-%m-%d")
                elif(periodo == 'ANUAL'):
                    print(datetime.now() + timedelta(days=365))
                    request.data['fecha_cancelacion'] = (datetime.now() + timedelta(days=365)).strftime("%Y-%m-%d")
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=partial)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            request.data._mutable = False
            return Response(serializer.data)
            
    def get_queryset(self):
        cod_cliente = self.request.query_params.get('cod_cliente')
        print(cod_cliente)
        if(cod_cliente == None):
            return facturacion.objects.all()
        else:
            return facturacion.objects.filter(cod_cliente=cod_cliente)
