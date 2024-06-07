# gemini_app/urls.py
from django.urls import path
from .views import UploadOrderView

urlpatterns = [
    path('', UploadOrderView.as_view(), name='upload_order'),
]
