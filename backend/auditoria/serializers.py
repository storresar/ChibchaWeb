from rest_framework import serializers
from .models import auditoria

class auditoria_serializer(serializers.ModelSerializer):
    class Meta:
        model = auditoria
        fields = '__all__'
        