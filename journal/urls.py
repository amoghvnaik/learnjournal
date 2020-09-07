from django.urls import path
from . import views
from .models import Resource

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('edit/<int:id>', views.edit, name='edit'),
]
