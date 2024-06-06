from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Bodega, Inventario, MovimientoInventario
from .forms import InventarioForm, MovimientoInventarioForm, BodegaForm

class InventarioListView(LoginRequiredMixin, ListView):
    model = Inventario
    template_name = 'inventario/inventario_list.html'
    context_object_name = 'inventarios'

class InventarioCreateView(LoginRequiredMixin, CreateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioUpdateView(LoginRequiredMixin, UpdateView):
    model = Inventario
    form_class = InventarioForm
    template_name = 'inventario/inventario_form.html'
    success_url = reverse_lazy('inventario_list')

class InventarioDeleteView(LoginRequiredMixin, DeleteView):
    model = Inventario
    template_name = 'inventario/inventario_confirm_delete.html'
    success_url = reverse_lazy('inventario_list')


class MovimientoInventarioListView(LoginRequiredMixin, ListView):
    model = MovimientoInventario
    template_name = 'inventario/movimiento_inventario_list.html'
    context_object_name = 'movimientos'

class MovimientoInventarioCreateView(LoginRequiredMixin, CreateView):
    model = MovimientoInventario
    form_class = MovimientoInventarioForm
    template_name = 'inventario/movimiento_inventario_form.html'
    success_url = reverse_lazy('movimiento_inventario_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        movimiento = form.save()
        # Actualizar inventario
        inventario = movimiento.inventario
        if movimiento.tipo == 'entrada':
            inventario.cantidad += movimiento.cantidad
        elif movimiento.tipo == 'salida':
            inventario.cantidad -= movimiento.cantidad
        inventario.save()
        return response

class BodegaListView(LoginRequiredMixin, ListView):
    model = Bodega
    template_name = 'inventario/bodega_list.html'
    context_object_name = 'bodegas'

class BodegaCreateView(LoginRequiredMixin, CreateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/bodega_form.html'
    success_url = reverse_lazy('bodega_list')

class BodegaUpdateView(LoginRequiredMixin, UpdateView):
    model = Bodega
    form_class = BodegaForm
    template_name = 'inventario/bodega_form.html'
    success_url = reverse_lazy('bodega_list')

class BodegaDeleteView(LoginRequiredMixin, DeleteView):
    model = Bodega
    template_name = 'inventario/bodega_confirm_delete.html'
    success_url = reverse_lazy('bodega_list')