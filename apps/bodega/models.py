from django.db import models

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
