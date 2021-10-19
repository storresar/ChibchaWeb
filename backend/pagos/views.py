from rest_framework import viewsets
from .models import facturacion
from .serializers import facturacion_serializer

# Create your views here.
class facturacion_viewset(viewsets.ModelViewSet):
    queryset = facturacion.objects.all()
    serializer_class = facturacion_serializer
