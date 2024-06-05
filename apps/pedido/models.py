from django.db import models
from calzado.models import Calzado  # Asegúrate de importar el modelo Calzado correctamente

class Pedido(models.Model):
    numero_pedido = models.CharField(max_length=50, unique=True)
    bloque = models.CharField(max_length=50)
    tipo_servicio = models.CharField(max_length=100, choices=[
        ('pegado', 'Pegado'),
        ('troquelado', 'Troquelado'),
        ('marcado', 'Marcado'),
    ])
    fecha_pedido = models.DateField()
    fecha_entrega = models.DateField()
    cliente = models.CharField(max_length=100)
    referencia_calzado = models.ForeignKey(Calzado, on_delete=models.CASCADE)  # Asegúrate de que la referencia a Calzado sea correcta
    lista_pares = models.JSONField()
    total_pares = models.IntegerField()
