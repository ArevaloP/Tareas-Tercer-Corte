from django.shortcuts import render, redirect
from .forms import MaestroForm

def  index(request):
	return render(request, '../templates/index.html')

def crearMaestro(request):
	if (request.method == 'POST'):
		maestro_form = MaestroForm(request.POST)
		if (maestro_form.is_valid()):
			maestro_form.save()
			return redirect('index')

	else:
		maestro_form = MaestroForm()
		print(maestro_form)

	return render(request, 'maestro/create_maestro.html',{'maestro_form':maestro_form})
