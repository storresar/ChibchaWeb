# Generated by Django 3.2.2 on 2021-10-19 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0003_alter_facturacion_fecha_cancelacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturacion',
            name='dominios_disponibles',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
