from django.contrib import admin
from django.urls import path, include
from SitioWeb import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('SitioWeb/', include('SitioWeb.urls')),
    path('', views.index, name='index')
]