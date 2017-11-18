from django import forms
from .models import TextUpload

class TextUploadForm(forms.ModelForm):
    class Meta:
        model = TextUpload
        fields = ('id', 'text',)
