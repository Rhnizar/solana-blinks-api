from django.urls import path
from . import views

urlpatterns = [
    path('Test/', views.Test, name='Test'),
]