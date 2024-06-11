from django import forms
from .models import Pedido
import json

class PedidoForm(forms.ModelForm):
    talla_34 = forms.IntegerField(min_value=0, required=False, label="Talla 34", initial=0)
    talla_35 = forms.IntegerField(min_value=0, required=False, label="Talla 35", initial=0)
    talla_36 = forms.IntegerField(min_value=0, required=False, label="Talla 36", initial=0)
    talla_37 = forms.IntegerField(min_value=0, required=False, label="Talla 37", initial=0)
    talla_38 = forms.IntegerField(min_value=0, required=False, label="Talla 38", initial=0)
    talla_39 = forms.IntegerField(min_value=0, required=False, label="Talla 39", initial=0)
    talla_40 = forms.IntegerField(min_value=0, required=False, label="Talla 40", initial=0)
    talla_41 = forms.IntegerField(min_value=0, required=False, label="Talla 41", initial=0)

    class Meta:
        model = Pedido
        fields = ['numero_pedido', 'bloque', 'tipo_servicio', 'fecha_entrega', 'cliente', 'referencia_calzado', 'total_pares']
        widgets = {
            'fecha_entrega': forms.TextInput(attrs={'type': 'text', 'class': 'flatpickr'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.lista_pares:
            lista_pares = json.loads(self.instance.lista_pares)  # Convierte la cadena JSON a un diccionario
            for item in lista_pares:
                talla = item['modelo']
                cantidad = item['cantidad']
                self.fields[f'talla_{talla}'].initial = cantidad

    def clean(self):
        cleaned_data = super().clean()
        lista_pares = []
        for talla in range(34, 42):
            cantidad = cleaned_data.get(f'talla_{talla}', 0)
            if cantidad is not None:
                lista_pares.append({"modelo": str(talla), "cantidad": cantidad})
        cleaned_data['lista_pares'] = json.dumps(lista_pares)  # Convierte la lista de pares a formato JSON
        cleaned_data['total_pares'] = sum(item['cantidad'] for item in lista_pares)
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.lista_pares = self.cleaned_data['lista_pares']
        instance.total_pares = self.cleaned_data['total_pares']
        if commit:
            instance.save()
        return instance
