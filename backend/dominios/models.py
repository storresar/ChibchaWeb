from django.db import models
from pagos.models import facturacion

# Create your models here.
class categoriaDistribuidor(models.Model):
    nom_categoria = models.CharField(max_length = 50)
    porcentaje_ganancia = models.PositiveSmallIntegerField(default=1)
    
class distribuidor(models.Model):
    nom_distribuidor = models.CharField(max_length = 50) 
    cod_categoria = models.ForeignKey(categoriaDistribuidor,on_delete=models.DO_NOTHING)

class dominio(models.Model):
    nom_dominio = models.CharField(max_length = 50)
    link_dominio = models.CharField(max_length = 50)
    cod_facturacion = models.ForeignKey(facturacion,on_delete=models.DO_NOTHING)
    cod_distribuidor = models.ForeignKey(distribuidor,on_delete=models.DO_NOTHING,null=True)
