from rest_framework import viewsets
from .models import usuario
from .serializers import usuario_serializer
from django.core.mail import send_mail
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
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
        #request.data._mutable = True
        request.data['password'] = make_password(request.data['password']) 
        #request.data._mutable = False
        return super(UsuarioViewSet, self).create(request)

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })