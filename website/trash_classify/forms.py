# forms.py
from django import forms
from .models import HisData


class ImgUploadForm(forms.ModelForm):
    class Meta:
        model = HisData
        fields = ['image']  # Only include the 'image' field for user input
