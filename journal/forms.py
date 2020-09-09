from django import forms
from django.forms import ModelForm
from .models import Resources

class ResourceForm(ModelForm):
    class Meta:
        model = Resources
        fields = '__all__'
