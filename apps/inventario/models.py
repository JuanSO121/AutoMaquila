from django.db import models
from bodega.models import Bodega
from calzado.models import Calzado

class InventarioBodega(models.Model):
    TALLA_CHOICES = [(str(i), str(i)) for i in range(34, 42)]
    
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    calzado = models.ForeignKey(Calzado, on_delete=models.CASCADE)
    talla = models.CharField(max_length=2, choices=TALLA_CHOICES)
    cantidad = models.IntegerField()
    
    class Meta:
        unique_together = ('bodega', 'calzado', 'talla')
    
    def __str__(self):
        return f"{self.bodega} - {self.calzado.nombre} - Talla {self.talla}: {self.cantidad} pares"
