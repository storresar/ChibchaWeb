# Generated by Django 3.2.2 on 2021-10-21 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0003_alter_ticket_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='solucionado',
            field=models.BooleanField(default=False),
        ),
    ]
