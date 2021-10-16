from django.db import models
from usuarios.models import usuario,cliente,empleado

# Create your models here.


class ticket(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.DO_NOTHING)
    vendedor = models.ForeignKey(empleado, on_delete=models.DO_NOTHING,null=True)
    desc_problema = models.CharField(max_length=50)
    desc_solucion = models.CharField(max_length=50)
    nivel = models.PositiveSmallIntegerField(default=1)
    solucionado = models.BooleanField()
