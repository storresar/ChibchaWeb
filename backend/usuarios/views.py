from rest_framework import viewsets,status
from .models import usuario
from .serializers import usuario_serializer
from django.core.mail import send_mail
from rest_framework.views import APIView
from django.contrib.auth import authenticate, login, logout
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuario_serializer

    def create(self, request):
        mensaje = '¡Felicidades! Usted se ha registrado exitosamente en ChibchaWeb.\n'
        mensaje += 'A continuacion mostaremos sus credenciales, por favor no las difunda con nadie mas.'
        mensaje += '\nUsuario:  ' + request.data['username'] + '\n'
        mensaje += 'Contraseña:  ' + request.data['password'] + '\n'
        send_mail(subject='Creacion de cuenta',message=mensaje,from_email=None,recipient_list=[request.data['email']])   
        request.data['password'] = make_password(request.data['password']) 
        return super(UsuarioViewSet, self).create(request)