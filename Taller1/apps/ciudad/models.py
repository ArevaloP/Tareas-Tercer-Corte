from django.db import models

# Create your models here.

class Ciudad(models.Model):
	CodigoPostal = models.IntegerField(primary_key=True)
	nombre = models.CharField(max_length=50)
	Temperatura = models.IntegerField()