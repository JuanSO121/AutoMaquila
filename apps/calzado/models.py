from django.db import models

class Calzado(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'calzado'
