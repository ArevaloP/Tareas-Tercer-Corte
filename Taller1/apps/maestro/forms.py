from django import forms
from .models import Maestro

class MaestroForm(forms.ModelForm):
	class Meta:
		model = Maestro
		fields = ['documento','nombre','apellido','colegio']