from django.db import models
from apps.colegio.models import Colegio
# Create your models here.
class Estudiante(models.Model):
	Documento = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	sexo = models.CharField(max_length=1)
	nacimiento = models.DateField()
	colegio = models.ForeignKey(Colegio, null=True, blank=True, on_delete=models.CASCADE)