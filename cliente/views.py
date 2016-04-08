from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .models import Cliente
from .forms import AgregarCliente

def agregar_cliente(request):
	if request.method == 'POST':
		form = AgregarCliente(request.POST, request.FILES)
		if form.is_valid():
			cliente = form.save()
			cliente.save()
			return HttpResponseRedirect('/')
	else:
		form = AgregarCliente

	template = loader.get_template("agregar_cliente.html")
	contex = {
		'title': 'Agregar Cliente',
		'form': form
	}
	return HttpResponse(template.render(contex,request))
