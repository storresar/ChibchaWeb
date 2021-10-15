from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.
class tipo_usuario(models.Model):
    nombre_rol = models.TextField(max_length=50)

    def __str__(self):
        return self.nombre_rol
        
class usuario(AbstractUser):
    intentos_loggeo = models.PositiveSmallIntegerField(default=0)
    rol = models.ForeignKey(tipo_usuario, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.username

class cliente(models.Model):
    cod_usuario = models.OneToOneField(usuario, on_delete=models.CASCADE, null=False)
    cod_plan = models.PositiveSmallIntegerField(default=0)
    cod_tipo_tarjeta = models.PositiveSmallIntegerField(default=0)
    num_tarjeta = models.TextField(max_length=50)
    cvv = models.TextField(max_length=50)

class empleado(models.Model):
    cod_usuario = models.OneToOneField(usuario, on_delete=models.CASCADE, null=False)
    nivel_empleado = models.PositiveSmallIntegerField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
