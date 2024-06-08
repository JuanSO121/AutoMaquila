from django.urls import path
from .views import PedidoListView, PedidoCreateView, PedidoUpdateView, PedidoDeleteView

urlpatterns = [
    path('', PedidoListView.as_view(), name='pedido_list'),
    path('create/', PedidoCreateView.as_view(), name='pedido_create'),
    path('update/<int:pk>/', PedidoUpdateView.as_view(), name='pedido_update'),
    path('delete/<int:pk>/', PedidoDeleteView.as_view(), name='pedido_delete'),
]
