from django.db import models

# Create your models here.

class Curso(models.Model):
    nombreCurso = models.CharField(max_length=30)

    def __str__(self):
        return self.nombreCurso


class Consulta(models.Model):
    id_consulta = models.AutoField(db_column='idConsulta', primary_key=True)
    nombre_c = models.CharField(max_length=20)
    apellido_c = models.CharField(max_length=20)
    numero_c = models.IntegerField()
    correo_c = models.EmailField(max_length=254)
    apoderado_c = models.BooleanField(default=False)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT, blank=True, null=True)
    consulta_c = models.TextField()
    estado_c = models.BooleanField(default=False)
    respuesta_c = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre_c

    class Meta:
        db_table = 'SitioWeb_consulta'

class Profesor(models.Model):
    nombre_prof = models.CharField(max_length=20)
    apellido_prof = models.CharField(max_length=20)
    correo_prof = models.EmailField(max_length=254)
    fec_contra_prof = models.DateField()
    
    def __str__(self):
        return self.nombre_prof

    class Meta:
        db_table = 'SitioWeb_profesor'
