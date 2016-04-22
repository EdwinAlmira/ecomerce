from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from productos.models import Categoria, Producto

# definimos una funcion para obtener una vista en el frontend
def index(request):
    template = loader.get_template('index.html')
    title = 'Inicio'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

def productos(request):
	template = loader.get_template('productos.html')
	title = 'Productos'
	categoria_list = Categoria.objects.all()
	productos_lista = Producto.objects.all()
	paginator = Paginator(productos_lista, 8)
	page = request.GET.get('page')
	try:
		productos_lista = paginator.page(page)
	except PageNotAnInteger:
		# If page is not an integer, deliver first page.
		productos_lista = paginator.page(1)
	except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
		productos_lista = paginator.page(paginator.num_pages)

	context = {
		'title' : title,
		'categoria_list': categoria_list,
		'productos_lista' : productos_lista,
		'paginator': paginator,
	}
	return HttpResponse(template.render(context,request))    

def compra(request):
	template = loader.get_template('compra.html')
	title = 'Compra'
	context = {
		'title' : title
	}
	return HttpResponse(template.render(context,request)) 

def conocenos(request):
	template = loader.get_template('conocenos.html')
	title = 'Vision y Mision'
	context = {
		'title' : title
	}
	return HttpResponse(template.render(context,request))    

def preguntas(request):
	template = loader.get_template('preguntas.html')
	title = 'Preguntas Frecuentes'
	context = {
		'title' : title
	}
	return HttpResponse(template.render(context,request))    