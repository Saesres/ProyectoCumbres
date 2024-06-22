from django import forms
from .models import Profesor


class profesorForm(forms.ModelForm):

    class Meta:
        model = Profesor
        fields = '__all__'
         
        widgets = {
            "fec_contra_prof": forms.SelectDateWidget()
        }