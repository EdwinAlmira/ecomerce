from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

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
	context = {
		'title' : title
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