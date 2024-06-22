from django.db import models

# Create your models here.
class consulta(models.Model):
    id_consulta = models.AutoField(db_column='idConsulta', primary_key=True)
    nombre_c = models.CharField(max_length = 20)
    apellido_c = models.CharField(max_length = 20)
    numero_c = models.IntegerField()
    correo_c = models.EmailField(max_length = 254)
    consulta_c = models.TextField()

class utp (models.Model):
    nombre_utp = models.CharField(max_length = 20)
    apellido_utp = models.CharField(max_length = 20)
    correo_utp = models.EmailField(max_length = 254)
    fec_contra_utp = models.DateField()

class curso (models.Model):
    nombre_curso = models.CharField(max_length = 25)
    id_curso= models.AutoField(db_column='idCurso', primary_key=True)
    curso = models.IntegerField()
    
    
class Video(models.Model):
    titulo_vid = models.CharField(max_length=100)
    descripcion_vid = models.TextField()

    def __str__(self):
        return self.titulo_vid


class Imagen(models.Model):
    titulo_img = models.CharField(max_length=70)
    descripcion_img = models.TextField()

    def __str__(self):
        return self.titulo_img
    
class Profesor(models.Model):
    nombre_prof = models.CharField(max_length=20)
    apellido_prof = models.CharField(max_length=20)
    correo_prof = models.EmailField(max_length=254)
    fec_contra_prof = models.DateField()

    class Meta:
        db_table = 'SitioWeb_profesor'


class Asistente(models.Model):
    nombre_asis = models.CharField(max_length=20)
    apellido_asis = models.CharField(max_length=20)
    correo_asis = models.CharField(max_length=254)
    fec_contra_asis = models.DateField()
