# Generated by Django 3.2.2 on 2021-10-24 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0007_auto_20211023_1926'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='is_respondido',
            field=models.BooleanField(default=False),
        ),
    ]