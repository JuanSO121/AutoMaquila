from django.db import models
from calzado.models import Calzado

class Bodega(models.Model):
    CIUDAD = [
        ('BOG', 'Bogotá'),
        ('MED', 'Medellín'),
        ('CALI', 'Cali'),
        ('B/Q', 'Barranquilla'),
        ('CART', 'Cartagena'),
        ('CUC', 'Cúcuta'),
        ('SOL', 'Soledad'),
        ('IBG', 'Ibagué'),
        ('BCM', 'Bucaramanga'),
        ('SOAC', 'Soacha'),
    ]
    
    pkBodega = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=128)
    ciudad = models.CharField(max_length=4, choices=CIUDAD, default='CALI')
    
    def __str__(self):
        return f"{self.ciudad} - {self.direccion}"

class Inventario(models.Model):
    TALLA_CHOICES = [(str(i), str(i)) for i in range(34, 42)]
    
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    calzado = models.ForeignKey(Calzado, on_delete=models.CASCADE)
    talla = models.CharField(max_length=2, choices=TALLA_CHOICES)
    cantidad = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ('bodega', 'calzado', 'talla')
    
    def __str__(self):
        return f"{self.bodega} - {self.calzado} - Talla {self.talla}: {self.cantidad}"
    
class MovimientoInventario(models.Model):
    TIPO_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
    ]
    
    inventario = models.ForeignKey(Inventario, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=7, choices=TIPO_MOVIMIENTO)
    cantidad = models.PositiveIntegerField()
    fecha = models.DateTimeField(auto_now_add=True)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.inventario} - {self.tipo}: {self.cantidad} ({self.fecha})"
    


