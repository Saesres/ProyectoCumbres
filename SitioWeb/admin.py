from django.contrib import admin
from .models import Profesor

# Register your models here.
class ProfesorAdmin(admin.ModelAdmin):
    list_display = ['nombre_prof', 'apellido_prof', 'correo_prof', 'fec_contra_prof']


admin.site.register(Profesor, ProfesorAdmin)
