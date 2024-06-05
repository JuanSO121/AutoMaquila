from django.urls import path
from orders.views import *

urlpatterns = [
    path('', list_orders),
    path('new/', create_task)
]