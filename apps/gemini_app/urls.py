# apps/gemini_app/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gemini_view, name='gemini_upload'),
]
