from django.urls import path
from .views import crearCiudad

urlpatterns = [
    path('crearCiudad',crearCiudad,name='crearCiudad'),
]
