from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


from .models import Categoria
from .forms	import AgregarCategoria

def agregar_categoria(request):
	if request.method == 'POST':
		form = AgregarCategoria(request.POST, request.FILES)
		if form.is_valid():
			categoria = form.save(commit=False)
			categoria.save()
			return HttpResponseRedirect('/')
	else:
		form = AgregarCategoria

	template = loader.get_template("agregar_categoria.html")
	contex = {
		'form': form
	}
	return HttpResponse(template.render(contex,request))
