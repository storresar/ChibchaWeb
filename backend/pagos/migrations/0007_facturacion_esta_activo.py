# Generated by Django 3.2.2 on 2021-10-24 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pagos', '0006_auto_20211021_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='facturacion',
            name='esta_activo',
            field=models.BooleanField(default=True),
        ),
    ]