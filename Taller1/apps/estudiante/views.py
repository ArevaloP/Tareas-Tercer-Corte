from django.shortcuts import render, redirect
from .forms import EstudianteForm

def  index(request):
	return render(request, '../templates/index.html')

def crearEstudiante(request):
	if (request.method == 'POST'):
		estudiante_form = EstudianteForm(request.POST)
		if (estudiante_form.is_valid()):
			estudinate_form.save()
			return redirect('index')

	else:
		estudiante_form = EstudianteForm()
		print(estudiante_form)

	return render(request, 'estudiante/create_estudiante.html',{'estudiante_form':estudiante_form})
