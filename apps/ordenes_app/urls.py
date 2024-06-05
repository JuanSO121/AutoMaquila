from django.urls import path
from .views import OrdenPedidoListado, OrdenPedidoDetalle, OrdenPedidoCrear, OrdenPedidoActualizar, OrdenPedidoEliminar

urlpatterns = [
    path('', OrdenPedidoListado.as_view(), name='orden_pedido_list'),
    path('<int:pk>/', OrdenPedidoDetalle.as_view(), name='orden_pedido_detail'),
    path('crear/', OrdenPedidoCrear.as_view(), name='orden_pedido_create'),
    path('editar/<int:pk>/', OrdenPedidoActualizar.as_view(), name='orden_pedido_update'),
    path('eliminar/<int:pk>/', OrdenPedidoEliminar.as_view(), name='orden_pedido_delete'),
]
