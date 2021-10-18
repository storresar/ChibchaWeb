from rest_framework import serializers
from .models import usuario,empleado,cliente
from django.contrib.auth.hashers import make_password

class usuario_serializer(serializers.ModelSerializer):
    class Meta:
        model = usuario
        fields = ('id','username','password','first_name', 'last_name', 'email','rol','date_joined','intentos_loggeo','is_active')

        def validate_password(self, value):
            return make_password(value)

class empleadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleado
        fields = '__all__'

class cliente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = '__all__'