# Generated by Django 3.2.2 on 2021-10-24 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0010_alter_facturacion_esta_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facturacion',
            name='esta_activo',
            field=models.BooleanField(default=True),
        ),
    ]