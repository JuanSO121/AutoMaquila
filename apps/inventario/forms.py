from django import forms
from .models import Inventario, MovimientoInventario, Bodega

class BodegaForm(forms.ModelForm):
    class Meta:
        model = Bodega
        fields = ['direccion', 'ciudad']
        
class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['bodega', 'calzado', 'talla', 'cantidad']

class MovimientoInventarioForm(forms.ModelForm):
    class Meta:
        model = MovimientoInventario
        fields = ['inventario', 'tipo', 'cantidad', 'descripcion']
