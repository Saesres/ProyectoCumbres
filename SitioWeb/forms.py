from django import forms
from .models import Profesor, Consulta, Curso


class profesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = '__all__'
         
        widgets = {
            "fec_contra_prof": forms.SelectDateWidget()
        }

class consultaForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nombre_c', 'apellido_c', 'numero_c', 'correo_c', 'apoderado_c', 'curso', 'consulta_c']
        widgets = {
            'nombre_c': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido_c': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_c': forms.NumberInput(attrs={'class': 'form-control'}),
            'correo_c': forms.EmailInput(attrs={'class': 'form-control'}),
            'apoderado_c': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'curso': forms.Select(choices=[
                ('', 'Seleccione un curso'),
            ] + [(curso.id, curso.nombreCurso) for curso in Curso.objects.all()], attrs={'class': 'form-control'}),
            'consulta_c': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EstadoForm(forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['estado_c', 'respuesta_c']
        widgets = {
            'estado_c': forms.CheckboxInput(),
            'respuesta_c': forms.Textarea(attrs={'rows': 3}),
        }