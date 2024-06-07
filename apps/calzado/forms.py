from django import forms
from .models import Calzado,Categoria

class CalzadoForm(forms.ModelForm):
    class Meta:
        model = Calzado
        fields = ['referencia', 'nombre', 'descripcion', 'precio', 'rutaImagen', 'categoria']  # Incluye 'categoria'


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombreCategoria', 'rutaImagen']