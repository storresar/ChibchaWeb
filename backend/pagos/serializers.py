from rest_framework import serializers
from .models import facturacion,plan

class facturacion_serializer(serializers.ModelSerializer):
    class Meta:
        model = facturacion
        fields = '__all__'

class plan_Serializer(serializers.ModelSerializer):
    class Meta:
        model = plan
        fields = '__all__'