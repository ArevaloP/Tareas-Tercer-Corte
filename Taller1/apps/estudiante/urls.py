from django.urls import path
from .views import crearEstudiante

urlpatterns = [
    path('crearEstudiante',crearEstudiante,name='crearEstudiante'),
]
