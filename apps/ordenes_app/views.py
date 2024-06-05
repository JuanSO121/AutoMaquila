from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import OrdenPedido, ListaPares

# Lista de órdenes de pedido
class OrdenPedidoListado(ListView):
    model = OrdenPedido
    template_name = 'orden_pedido_list.html'

# Detalle de una orden de pedido
class OrdenPedidoDetalle(DetailView):
    model = OrdenPedido
    template_name = 'orden_pedido_detail.html'

# Crear una nueva orden de pedido
class OrdenPedidoCrear(CreateView):
    model = OrdenPedido
    fields = ['orden_pedido', 'bloque', 'fecha_orden', 'fecha_entrega', 'cliente', 'referencia', 'foto_orden']
    template_name = 'orden_pedido_form.html'
    success_url = reverse_lazy('orden_pedido_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['talla_range'] = range(34, 42)  # Aquí definimos el rango de tallas
        return context

    def form_valid(self, form):
        orden_pedido = form.save(commit=False)
        orden_pedido.save()

        lista_pares_data = self.request.POST.getlist('talla')
        pares_data = self.request.POST.getlist('pares')
        for talla, pares in zip(lista_pares_data, pares_data):
            try:
                ListaPares.objects.create(orden_pedido=orden_pedido, talla=talla, pares=pares)
            except Exception as e:
                pass

        return super().form_valid(form)

# Actualizar una orden de pedido
class OrdenPedidoActualizar(UpdateView):
    model = OrdenPedido
    fields = ['orden_pedido', 'bloque', 'fecha_orden', 'fecha_entrega', 'cliente', 'referencia', 'foto_orden']
    template_name = 'orden_pedido_form.html'
    success_url = reverse_lazy('orden_pedido_list')

# Eliminar una orden de pedido
class OrdenPedidoEliminar(DeleteView):
    model = OrdenPedido
    template_name = 'orden_pedido_confirm_delete.html'
    success_url = reverse_lazy('orden_pedido_list')
