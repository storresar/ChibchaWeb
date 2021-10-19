from rest_framework import serializers
from .models import dominio

class dominio_Serializer(serializers.ModelSerializer):
    class Meta:
        model = dominio
        fields = '__all__'