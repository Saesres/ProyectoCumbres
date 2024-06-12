from django.urls import path
from .views import index, Contacto

urlpatterns = [
    path('index', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
]
