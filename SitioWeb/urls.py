from django.urls import path
from .views import index, Contacto, agregarProfesor, listarProfesor

urlpatterns = [
    path('index', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
    path('agregarProfesor', agregarProfesor, name='agregarProfesor'),
    path('listarProfesor', listarProfesor, name='listarProfesor'),
]
