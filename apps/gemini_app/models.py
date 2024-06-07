# gemini_app/models.py
from django.db import models

class UserUpload(models.Model):
    description = models.CharField(max_length=255)
    file = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
