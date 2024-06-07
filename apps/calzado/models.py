from django.db import models

class Calzado(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    rutaImagen = models.ImageField(upload_to = '../media/calzado_imagenes/', blank=True, null=True, default='../media/calzado_imagenes/zapato.png')###############
    
    def __str__(self):
        return f"{self.nombre} ({self.precio})"

    class Meta:
        app_label = 'calzado'
        
class Categoria(models.Model):
    pkCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=256, unique=True)
    rutaImagen = models.ImageField(upload_to = '../uploads', default='../uploads/zapato.png')
    
    def __str__(self):
        return f"{self.nombreCategoria}"
    
    
