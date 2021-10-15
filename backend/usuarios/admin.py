from django.contrib import admin
from .models import usuario,tipo_usuario,cliente,empleado
# Register your models here.

admin.site.register(usuario)
admin.site.register(tipo_usuario)
admin.site.register(cliente)
admin.site.register(empleado)