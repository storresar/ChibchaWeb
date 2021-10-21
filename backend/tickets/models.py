from django.db import models
from usuarios.models import usuario,empleado
from django.conf import settings


# Create your models here.


class ticket(models.Model):
    cod_cliente = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    cod_vendedor = models.ForeignKey(empleado, on_delete=models.DO_NOTHING,null=True)
    desc_problema = models.CharField(max_length=350)
    desc_solucion = models.CharField(max_length=350)
    nivel = models.PositiveSmallIntegerField(default=1)
    solucionado = models.BooleanField(default=False)

