from django.contrib import admin
from django.urls import path, include
from SitioWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SitioWeb/', include('SitioWeb.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.index, name='index')
]

admin.site.site_header = "Administración Colegio Cumbres de Placilla"
admin.site.index_title = "Modulos de Administración"
admin.site.site_title = "Cumbres de Placilla"