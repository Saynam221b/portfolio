from django import forms
from .models import UploadedFile

class UploadFileForm(forms.Form):
    csv_file = forms.FileField()