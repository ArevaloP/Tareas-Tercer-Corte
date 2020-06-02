from django.urls import path
from .views import crearMaestro

urlpatterns = [
    path('crearMaestro',crearMaestro,name='crearMaestro'),
]
