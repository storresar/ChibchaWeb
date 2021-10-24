from django.shortcuts import render
from rest_framework import viewsets
from .models import dominio
from .serializers import dominio_Serializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from pagos.models import facturacion
from rest_framework import status

# Create your views here.

class dominio_viewSet(viewsets.ModelViewSet):
    queryset = dominio.objects.all()
    serializer_class = dominio_Serializer

    def create(self, request, *args, **kwargs):
        factura = get_object_or_404(facturacion.objects.filter(pk = request.data['cod_facturacion']))
        disponibles = factura.dominios_disponibles
        if(disponibles == 0):
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            actualizacion = facturacion(
                    pk = request.data['cod_facturacion'],
                    cod_cliente = factura.cod_cliente,
                    cod_plan = factura.cod_plan, 
                    valor_total= factura.valor_total,
                    dominios_disponibles = (factura.dominios_disponibles -1),
                    fecha_facturacion = factura.fecha_facturacion,
                    fecha_cancelacion = factura.fecha_cancelacion,
                )
            actualizacion.save()
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data)

    def get_queryset(self):
        cod_facturacion = self.request.query_params.get('cod_facturacion')
        print(cod_facturacion)
        if(cod_facturacion == None):
            return dominio.objects.all()
        else:
            return dominio.objects.filter(cod_facturacion=cod_facturacion)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instace2 = dominio.objects.get(pk=self.kwargs["pk"])
        factura = get_object_or_404(facturacion.objects.filter(pk = instace2.cod_facturacion.pk))
        nuevos_dom = factura.dominios_disponibles+1
        nueva_factura = facturacion(
            pk = factura.id,
            valor_total = factura.valor_total,
            dominios_disponibles  =  nuevos_dom,
            fecha_facturacion = factura.fecha_facturacion,
            fecha_cancelacion = factura.fecha_cancelacion,
            esta_activo = factura.esta_activo,
            cod_cliente = factura.cod_cliente,
            cod_plan = factura.cod_plan

        )
        nueva_factura.save()
        self.perform_destroy(instance)
        return self.list(request)