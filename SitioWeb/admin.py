from django.contrib import admin
from .models import Profesor, consulta

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre_prof', 'apellido_prof', 'correo_prof', 'fec_contra_prof']

admin.site.register(Profesor, ProfesorAdmin)

class consultaAdmin(admin.ModelAdmin):
    list_display = ['nombre_c', 'apellido_c', 'numero_c', 'correo_c', 'consulta_c']

admin.site.register(consulta, consultaAdmin)
