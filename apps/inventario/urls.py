from django.urls import path
from .views import (
    BodegaListView, BodegaCreateView, BodegaUpdateView, BodegaDeleteView,
    InventarioListView, InventarioCreateView, InventarioUpdateView, InventarioDeleteView,
    MovimientoInventarioListView, MovimientoInventarioCreateView
)

urlpatterns = [
    path('', InventarioListView.as_view(), name='inventario_list'),
    path('inventarios/new/', InventarioCreateView.as_view(), name='inventario_create'),
    path('inventarios/<int:pk>/edit/', InventarioUpdateView.as_view(), name='inventario_update'),
    path('inventarios/<int:pk>/delete/', InventarioDeleteView.as_view(), name='inventario_delete'),

    path('movimientos/', MovimientoInventarioListView.as_view(), name='movimiento_inventario_list'),
    path('movimientos/new/', MovimientoInventarioCreateView.as_view(), name='movimiento_inventario_create'),
    
    path('bodegas/', BodegaListView.as_view(), name='bodega_list'),
    path('bodegas/new/', BodegaCreateView.as_view(), name='bodega_create'),
    path('bodegas/<int:pk>/edit/', BodegaUpdateView.as_view(), name='bodega_update'),
    path('bodegas/<int:pk>/delete/', BodegaDeleteView.as_view(), name='bodega_delete'),
]
