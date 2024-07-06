from django import forms
from .models import Profesor, consulta


class profesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = '__all__'
         
        widgets = {
            "fec_contra_prof": forms.SelectDateWidget()
        }

class consultaForm(forms.ModelForm):

    class Meta:
        model = consulta
        fields = '__all__'
         