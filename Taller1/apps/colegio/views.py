from django.shortcuts import render, redirect
from .forms import ColegioForm

def  index(request):
	return render(request, '../templates/index.html')

def crearColegio(request):
	if (request.method == 'POST'):
		colegio_form = ColegioForm(request.POST)
		if (colegio_form.is_valid()):
			colegio_form.save()
			return redirect('index')

	else:
		colegio_form = ColegioForm()
		print(colegio_form)

	return render(request, 'colegio/create_colegio.html',{'colegio_form':colegio_form})
