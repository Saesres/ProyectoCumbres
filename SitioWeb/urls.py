from django.urls import path
from .views import index, Contacto, agregarProfesor, listarProfesor, modificarProfesor, eliminarProfesor, listarConsulta, eliminarConsulta, estadoConsulta

urlpatterns = [
    path('index', index, name='index'),
    path('Contacto', Contacto, name='Contacto'),
    path('agregarProfesor', agregarProfesor, name='agregarProfesor'),
    path('listarProfesor', listarProfesor, name='listarProfesor'),
    path('modificarProfesor/<int:id>', modificarProfesor, name='modificarProfesor'),
    path('eliminarProfesor/<int:id>', eliminarProfesor, name='eliminarProfesor'),
    path('listarConsulta', listarConsulta, name='listarConsulta'),
    path('estadoConsulta/<int:id>', estadoConsulta, name='estadoConsulta'),
    path('eliminarConsulta/<int:id>', eliminarConsulta, name='eliminarConsulta'),
]
