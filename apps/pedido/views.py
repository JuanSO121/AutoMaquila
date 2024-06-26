from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Pedido
from .forms import PedidoForm

class PedidoListView(LoginRequiredMixin, ListView):
    model = Pedido
    template_name = 'pedido/pedido_list.html'
    context_object_name = 'pedidos'

class PedidoCreateView(LoginRequiredMixin, CreateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

class PedidoUpdateView(LoginRequiredMixin, UpdateView):
    model = Pedido
    form_class = PedidoForm
    template_name = 'pedido/pedido_form.html'
    success_url = reverse_lazy('pedido_list')

class PedidoDeleteView(LoginRequiredMixin, DeleteView):
    model = Pedido
    template_name = 'pedido/pedido_confirm_delete.html'
    success_url = reverse_lazy('pedido_list')
