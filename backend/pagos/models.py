from django.db import models
from usuarios.models import cliente

# Create your models here.
class plan(models.Model):
    nom_plan = models.CharField(max_length = 50)
    valor_plan = models.IntegerField(default=0)
    periodo_fact = models.CharField(max_length=10)
    cant_dominios = models.PositiveSmallIntegerField(default=0)
    cant_correos = models.PositiveSmallIntegerField(default=0)
    capacidad = models.PositiveSmallIntegerField(default=0)
    hasSSL =  models.BooleanField()
    cant_db = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.nom_plan
    
class facturacion(models.Model):
    cod_cliente = models.OneToOneField(cliente , on_delete = models.DO_NOTHING,null=False)
    cod_plan = models.ForeignKey(plan , on_delete = models.DO_NOTHING,null=False)
    valor_total = models.IntegerField(default=0)
    dominios_disponibles = models.PositiveSmallIntegerField(default=0)
    fecha_facturacion = models.DateField(auto_now=False,null=True)
    fecha_cancelacion = models.DateField(auto_now=False,null=True)
    esta_activo = models.BooleanField(default=True)



