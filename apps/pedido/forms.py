from django import forms
from .models import Pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'bloque', 'tipo_servicio', 'fecha_entrega', 'cliente', 'referencia_calzado', 'lista_pares', 'total_pares']
