from django import forms
from .models import Profesor, Consulta


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
            'numero_c': forms.NumberInput(attrs={'class': 'form-control'}),
            'apoderado_c': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'consulta_c': forms.TextInput(attrs={'class': 'form-control'}),
        }