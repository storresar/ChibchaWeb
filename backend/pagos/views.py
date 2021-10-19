from rest_framework import viewsets
from .models import facturacion,plan
from .serializers import facturacion_serializer
from rest_framework.response import Response
from datetime import datetime,timedelta
from django.shortcuts import get_object_or_404
from usuarios.models import cliente,usuario
from auditoria.models import auditoria
from django.core.mail import send_mail

# Create your views here.
class facturacion_viewset(viewsets.ModelViewSet):
    queryset = facturacion.objects.all()
    serializer_class = facturacion_serializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
            plan_escogido = get_object_or_404(plan.objects.filter(pk = request.data['cod_plan']))
            periodo =  plan_escogido.periodo_fact
            cod_cliente = get_object_or_404(cliente.objects.filter(pk = request.data['cod_cliente'])).cod_usuario
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
                nueva_auditoria = auditoria(
                    tipo = 'Facturación agregada', 
                    ip=request.META.get('REMOTE_ADDR'),
                    usuario_realiza=cod_cliente,
                    area_afectada = 'FACTURACIÓN'
                )
                nueva_auditoria.save()
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data)