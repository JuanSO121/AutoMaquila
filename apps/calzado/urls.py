from django.urls import path
from .views import (
    CalzadoListView,
    CalzadoDetailView,
    CalzadoCreateView,
    CalzadoUpdateView,
    CalzadoDeleteView,
)

urlpatterns = [
    path('', CalzadoListView.as_view(), name='calzado_list'),
    path('<int:pk>/', CalzadoDetailView.as_view(), name='calzado_detail'),
    path('nuevo/', CalzadoCreateView.as_view(), name='calzado_create'),
    path('editar/<int:pk>/', CalzadoUpdateView.as_view(), name='calzado_update'),
    path('eliminar/<int:pk>/', CalzadoDeleteView.as_view(), name='calzado_delete'),
]
