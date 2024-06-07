from django.db import models
from calzado.models import Calzado  # Asegúrate de importar el modelo Calzado correctamente

class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=50, unique=True, default='N/A')
    bloque = models.CharField(max_length=50, default='Sin Bloque')
    tipo_servicio = models.CharField(max_length=100, choices=[
        ('pegado', 'Pegado'),
        ('troquelado', 'Troquelado'),
        ('marcado', 'Marcado'),
    ], default='pegado')
    fecha_pedido = models.DateField(auto_now_add=True)
    fecha_entrega = models.DateField(null=True, blank=True)
    cliente = models.CharField(max_length=100, default='Cliente Anónimo')
    referencia_calzado = models.ForeignKey(Calzado, on_delete=models.CASCADE, null=True, blank=True)  # Asegúrate de que la referencia a Calzado sea correcta
    lista_pares = models.JSONField(default=dict)
    total_pares = models.IntegerField(default=0)

    def __str__(self):
        return f'Pedido {self.numero_pedido} para {self.cliente}'
