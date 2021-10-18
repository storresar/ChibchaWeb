from rest_framework import viewsets
from .models import usuario,empleado,cliente
from .serializers import usuario_serializer,empleadoSerializer,cliente_Serializer
from django.core.mail import send_mail
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from auditoria.models import auditoria
# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = usuario.objects.all()
    serializer_class = usuario_serializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        contrasenia = request.data['password']
        request.data['password'] = make_password(request.data['password'])
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if(serializer.is_valid):
            mensaje = '¡Felicidades! Usted se ha registrado exitosamente en ChibchaWeb.\n'
            mensaje += 'A continuacion mostaremos sus credenciales, por favor no las difunda con nadie mas.'
            mensaje += '\nUsuario:  ' + request.data['username'] + '\n'
            mensaje += 'Contraseña:  ' + contrasenia + '\n'
            send_mail(subject='Creacion de cuenta',message=mensaje,from_email=None,recipient_list=[request.data['email']])
            nueva_auditoria = auditoria(
                tipo = 'Creación usuario', 
                ip=request.META.get('REMOTE_ADDR'),
                usuario_realiza=request.data['username'],
                area_afectada = 'USUARIOS'
            )
            nueva_auditoria.save()
        self.perform_create(serializer)
        #request.data._mutable = True 
        #request.data._mutable = False
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        request.data._mutable = True
        request.data['password'] = make_password(request.data['password']) 
        request.data._mutable = False
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        nueva_auditoria = auditoria(
                tipo = 'Modificación usuario', 
                ip=request.META.get('REMOTE_ADDR'),
                usuario_realiza=request.data['username'],
                area_afectada = 'USUARIOS'
            )
        nueva_auditoria.save()
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        nueva_auditoria = auditoria(
                tipo = 'Eliminación usuario', 
                ip=request.META.get('REMOTE_ADDR'),
                usuario_realiza= instance,
                area_afectada = 'USUARIOS'
            )
        nueva_auditoria.save()
        self.perform_destroy(instance)
        return self.list(request)

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

class empleado_viewset(viewsets.ModelViewSet):
    queryset = empleado.objects.all()
    serializer_class = empleadoSerializer

class cliente_viewset(viewsets.ModelViewSet):
    queryset = cliente.objects.all()
    serializer_class = cliente_Serializer