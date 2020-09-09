from django.urls import path
from . import views
from .models import Resources

urlpatterns = [
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('edit/<int:id>', views.edit, name='edit'),
]

