from django.db import models
from apps.colegio.models import Colegio
# Create your models here.
class Maestro(models.Model):
	documento = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	colegio = models.ForeignKey(Colegio, null=True, blank=True, on_delete=models.CASCADE)
