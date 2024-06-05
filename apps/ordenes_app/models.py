# models.py
from django.db import models
from django.db.models import Sum
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class OrdenPedido(models.Model):
    orden_pedido = models.CharField(max_length=10, unique=True)
    bloque = models.CharField(max_length=6)
    fecha_orden = models.DateField()
    fecha_entrega = models.DateField(blank=True, null=True)
    cliente = models.CharField(max_length=50)
    referencia = models.CharField(max_length=50)
    total_pares = models.IntegerField(editable=False, default=0)
    foto_orden = models.ImageField(upload_to='ordenes/', blank=True, null=True)
    
    def save(self, *args, **kwargs):
        self.total_pares = self.lista_pares.aggregate(models.Sum('pares'))['pares__sum'] or 0
        super().save(*args, **kwargs)
    
    class Meta:
        db_table = 'orden_pedido'
        verbose_name = 'Orden de Pedido'
        verbose_name_plural = 'Ordenes de Pedido'

class ListaPares(models.Model):
    TALLAS = [(str(i), str(i)) for i in range(34, 42)]
    orden_pedido = models.ForeignKey('OrdenPedido', related_name='lista_pares', on_delete=models.CASCADE)
    talla = models.CharField(max_length=2, choices=TALLAS)
    pares = models.IntegerField(default=0)

    class Meta:
        db_table = 'lista_pares'
        verbose_name = 'Lista de Pares'
        verbose_name_plural = 'Listas de Pares'

@receiver(post_save, sender=ListaPares)
@receiver(post_delete, sender=ListaPares)
def update_total_pares(sender, instance, **kwargs):
    orden_pedido = instance.orden_pedido
    orden_pedido.total_pares = orden_pedido.lista_pares.aggregate(total_pares=Sum('pares'))['total_pares'] or 0
    orden_pedido.save()
