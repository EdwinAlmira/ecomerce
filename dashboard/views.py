from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# importamos los modelos necesarios para realizar la autentificacion de usuarios
from login.models import MyUser, PersonalAdministrativo
from cliente.models import Cliente

# funcion cliente devuelve el dashboard para los clientes
def cliente(request,template,user):

# Obteneos el cliente ligado al usuario logeado	
	cliente = Cliente.objects.get(correo=user.email)
	
	client = cliente.nombre+ " " +cliente.apellido
	title = "Dashboard"
	context = {
	    'title': title,
	    'client': client
	}
	return HttpResponse(template.render(context, request))

# funcion cliente devuelve el dashboard para los administradores del sitio
def admin(request,template,user):
# Obtenemos el administrador ligado al usuario
	admin = PersonalAdministrativo.objects.get(correo=user.email)

	name = admin.nombre + " "+ admin.apellido

	title = "Dashboard-admin"
	context = {
	    'title': title,
	    'name': name
	}
	return HttpResponse(template.render(context, request))

# fucion para devolver una vista a un usuario autenticado
def login(request):
	# si el usuario no esta logeado 
	if not request.user.is_authenticated():
		return redirect('/login/')
	else:
		#obtenemos el usuario que esta logeado
		user = request.user
		#si el usuario no es del personal administrativo
		if not user.is_personal:
			template = loader.get_template('cliente_dash.html')
			return cliente(request,template,user)
		
		template = loader.get_template('admin_dash.html')
		return admin(request,template,user)
		
