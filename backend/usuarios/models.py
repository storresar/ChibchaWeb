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


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
