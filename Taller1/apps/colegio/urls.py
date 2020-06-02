from django.urls import path
from .views import crearColegio

urlpatterns = [
    path('crearColegio',crearColegio,name='crearColegio'),
]
