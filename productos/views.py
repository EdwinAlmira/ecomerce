from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# modelos y su respectivo formulario
from .models import Categoria, Proveedor, Producto
from .forms	import AgregarCategoria, AgregarProveedor, AgregarProducto

# funcion agregar categoria
def agregar_categoria(request):
	# verifica que el usuario este logeado
	if not request.user.is_authenticated():
		return redirect('/login/')

	user = request.user
	# si intenta guardarlo
	if request.method == 'POST':
		form = AgregarCategoria(request.POST)
		if form.is_valid():
			categoria = form.save()
			categoria.save()
		return HttpResponseRedirect('/dashboard/')
	# si el usuario admin intenta obtener la vista
	elif user.is_personal:
		form = AgregarCategoria()
		template = loader.get_template("agregar_categoria.html")
		contex = {
			'form': form
		}
		return HttpResponse(template.render(contex,request))

	#si el usuario no es del personal administrativo	
	return HttpResponseRedirect('/dashboard/')		


# funcion agregar proveedor
def agregar_proveedor(request):
	# verifica que el usuario este logeado
	if not request.user.is_authenticated():
		return redirect('/login/')

	user = request.user
	# si intenta guardarlo
	if request.method == 'POST':
		form = AgregarProveedor(request.POST, request.FILES)
		if form.is_valid():
			proveedor = form.save()
			proveedor.save()
		return HttpResponseRedirect('/dashboard/')
	# si el usuario admin intenta obtener la vista
	elif user.is_personal:
		form = AgregarProveedor()
		template = loader.get_template("agregar_proveedor.html")
		contex = {
			'form': form
		}
		return HttpResponse(template.render(contex,request))

	#si el usuario no es del personal administrativo	
	return HttpResponseRedirect('/dashboard/')		


# funcion agregar producto
def agregar_producto(request):
	# verifica que el usuario este logeado
	if not request.user.is_authenticated():
		return redirect('/login/')

	user = request.user
	# si intenta guardarlo
	if request.method == 'POST':
		form = AgregarProducto(request.POST, request.FILES)
		if form.is_valid():
			producto = form.save()
			producto.save()
		return HttpResponseRedirect('/dashboard/')
	# si el usuario admin intenta obtener la vista
	elif user.is_personal:
		form = AgregarProducto()
		template = loader.get_template("agregar_producto.html")
		contex = {
			'form': form
		}
		return HttpResponse(template.render(contex,request))

	#si el usuario no es del personal administrativo	
	return HttpResponseRedirect('/dashboard/')		
