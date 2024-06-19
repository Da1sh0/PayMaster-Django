from django.contrib import admin
from . models import Empresa, Empleado, Calculos, Novedades

admin.site.register(Empresa)
admin.site.register(Calculos)
admin.site.register(Empleado)
admin.site.register(Novedades)
# Register your models here.
