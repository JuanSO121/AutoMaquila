from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Calzado, Categoria
from .forms import CalzadoForm, CategoriaForm

class CalzadoListView(ListView):
    model = Calzado
    template_name = 'calzado/calzado_list.html'
    context_object_name = 'calzados'

class CalzadoDetailView(DetailView):
    model = Calzado
    template_name = 'calzado/calzado_detail.html'
    context_object_name = 'calzado'

class CalzadoCreateView(CreateView):
    model = Calzado
    form_class = CalzadoForm
    template_name = 'calzado/calzado_form.html'
    success_url = reverse_lazy('calzado_list')

class CalzadoUpdateView(UpdateView):
    model = Calzado
    form_class = CalzadoForm
    template_name = 'calzado/calzado_form.html'
    success_url = reverse_lazy('calzado_list')

class CalzadoDeleteView(DeleteView):
    model = Calzado
    template_name = 'calzado/calzado_confirm_delete.html'
    success_url = reverse_lazy('calzado_list')


class CategoriaListView(ListView):
    model = Categoria
    template_name = 'calzado/categoria_list.html'
    context_object_name = 'categorias'

class CategoriaDetailView(DetailView):
    model = Categoria
    template_name = 'calzado/categoria_detail.html'
    context_object_name = 'categoria'

class CategoriaCreateView(CreateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'calzado/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaUpdateView(UpdateView):
    model = Categoria
    form_class = CategoriaForm
    template_name = 'calzado/categoria_form.html'
    success_url = reverse_lazy('categoria_list')

class CategoriaDeleteView(DeleteView):
    model = Categoria
    template_name = 'calzado/categoria_confirm_delete.html'
    success_url = reverse_lazy('categoria_list')
