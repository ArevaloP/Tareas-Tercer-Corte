from django.db import models
from apps.ciudad.models import Ciudad
# Create your models here.

class Colegio(models.Model):
	ID = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	direccion = models.CharField(max_length=50)
	ciudad = models.ForeignKey(Ciudad, null=True, blank=True, on_delete=models.CASCADE)
	