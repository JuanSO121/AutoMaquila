# gemini_app/forms.py
from django import forms
from .models import UserUpload

class UploadFileForm(forms.ModelForm):
    class Meta:
        model = UserUpload
        fields = ['description', 'file']
