# gemini_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('hu_imagen/', views.hu_imagen, name='pedido_gemini'),
    path('download_document/<str:format>/', views.download_document, name='download_document'),
]
