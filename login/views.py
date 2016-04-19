from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# importa el modelo del cliente y el de autentifiacion(MyUser)
from cliente.models import Cliente
from login.models import MyUser

# importa el formulario para registrar un cliente
from .forms import Registrarme

# funcion para autentificar a los usuarios
def login(request):
    if request.method == 'POST':

        #Obtiene la password y correo del usuario
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        
        #Intenta autentificarse con el modelo de MyUser
        user = authenticate(email=email, password=password)

        #una vez se verifica el usuario, inicia sesion
        auth_login(request, user)
        # redirecciona al dashboard, el cual identificara el tipo de usuario
        return redirect('/dashboard/')
    else:
        #Peticion para cargar la vista
        template = loader.get_template("login.html")
        contex = {
        'title': 'Agregar Cliente',
        
        }
        return HttpResponse(template.render(contex,request))

# funcion para registrar un nuevo cliente
def singin(request):
    if request.method == 'POST':
        # Se crea un formulario y se rellena con el request
        form = Registrarme(request.POST, request.FILES)

        #se validan los datos del formulario
        if form.is_valid():
            
            #se obtiene el correo y contra para ser registrados en los usaurios
            email = request.POST.get('correo', None)
            password = request.POST.get('password', None)
            print password
            is_personal = False

            # se guarda el usuario tipo cliente en el modelo MyUser
            user = MyUser.objects.create_user(email=email,is_personal=is_personal, password=password)
            user.save()

            # se registra el cliente en el modelo cliente
            nuevo_cliente = form.save()
            nuevo_cliente.save()

            return HttpResponseRedirect('/')
    else:
        # peticion para la vista se obtiene el formulario
        form = Registrarme
    # se envia el formulario a la vista
    template = loader.get_template("singin.html")
    contex = {
        'title' : 'Registrarme',
        'form' : form
    }
    return HttpResponse(template.render(contex,request))