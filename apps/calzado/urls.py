
from django.urls import path
from .views import (
    CalzadoListView, CalzadoDetailView, CalzadoCreateView, CalzadoUpdateView, CalzadoDeleteView,
    CategoriaListView, CategoriaDetailView, CategoriaCreateView, CategoriaUpdateView, CategoriaDeleteView
)

urlpatterns = [
    path('', CalzadoListView.as_view(), name='calzado_list'),
    path('calzados/<int:pk>/', CalzadoDetailView.as_view(), name='calzado_detail'),
    path('calzados/new/', CalzadoCreateView.as_view(), name='calzado_create'),
    path('calzados/<int:pk>/edit/', CalzadoUpdateView.as_view(), name='calzado_update'),
    path('calzados/<int:pk>/delete/', CalzadoDeleteView.as_view(), name='calzado_delete'),

    path('categorias/', CategoriaListView.as_view(), name='categoria_list'),
    path('categorias/<int:pk>/', CategoriaDetailView.as_view(), name='categoria_detail'),
    path('categorias/new/', CategoriaCreateView.as_view(), name='categoria_create'),
    path('categorias/<int:pk>/edit/', CategoriaUpdateView.as_view(), name='categoria_update'),
    path('categorias/<int:pk>/delete/', CategoriaDeleteView.as_view(), name='categoria_delete'),
]
