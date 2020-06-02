from django.shortcuts import render, redirect
from .forms import CiudadForm

def  index(request):
	return render(request, '../templates/index.html')

def crearCiudad(request):
	if (request.method == 'POST'):
		ciudad_form = CiudadForm(request.POST)
		if (ciudad_form.is_valid()):
			ciudad_form.save()
			return redirect('index')

	else:
		ciudad_form = CiudadForm()
		print (ciudad_form)

	return render(request, 'ciudad/create_ciudad.html',{'ciudad_form':ciudad_form})
