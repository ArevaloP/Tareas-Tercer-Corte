from django import forms
from .models import Estudiante

class EstudianteForm(forms.ModelForm):
	class Meta:
		model = Estudiante
		fields = ['Documento','nombre','apellido','sexo','nacimiento','colegio']