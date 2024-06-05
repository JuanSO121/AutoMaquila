from django import forms
from .models import Calzado

class CalzadoForm(forms.ModelForm):
    class Meta:
        model = Calzado
        fields = ['referencia', 'nombre', 'descripcion', 'precio']
