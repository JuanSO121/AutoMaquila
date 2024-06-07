from django.db import models

class Categoria(models.Model):
    pkCategoria = models.AutoField(primary_key=True)
    nombreCategoria = models.CharField(max_length=256, unique=True)
    rutaImagen = models.ImageField(upload_to='media/', default='media/zapato.png')
    
    def __str__(self):
        return f"{self.nombreCategoria}"

class Calzado(models.Model):
    referencia = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    rutaImagen = models.ImageField(upload_to='media/', blank=True, null=True, default='media/calzado_imagenes/zapato.png')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='calzados', default=1)  # default se refiere a la pk de una categoría existente

    def __str__(self):
        return f"{self.nombre} ({self.precio})"

    class Meta:
        app_label = 'calzado'
