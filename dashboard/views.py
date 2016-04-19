from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from login.models import MyUser, PersonalAdministrativo
from cliente.models import Cliente
# funcion login devuelve la vista login
def cliente(request,template,user):

	cliente = Cliente.objects.get(correo=user.email)
	
	client = cliente.nombre+ " " +cliente.apellido
	title = "Dashboard"
	context = {
	    'title': title,
	    'client': client
	}
	return HttpResponse(template.render(context, request))

def admin(request,template,user):

	admin = PersonalAdministrativo.objects.get(correo=user.email)

	name = admin.nombre + " "+ admin.apellido

	title = "Dashboard-admin"
	context = {
	    'title': title,
	    'name': name
	}
	return HttpResponse(template.render(context, request))
	
def login(request):
	# si el usuario no esta logeado 
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		user = request.user
		if not user.is_personal:
			template = loader.get_template('cliente_dash.html')
			return cliente(request,template,user)
		
		template = loader.get_template('admin_dash.html')
		return admin(request,template,user)
		
