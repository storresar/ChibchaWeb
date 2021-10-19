from rest_framework import serializers
from .models import facturacion

class facturacion_serializer(serializers.ModelSerializer):
    class Meta:
        model = facturacion
        fields = '__all__'