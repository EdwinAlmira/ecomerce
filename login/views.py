from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

# se importan el modelo y el formulario

from cliente.models import Cliente
from login.models import MyUser
from .forms import Registrarme

def sample_view(request):
    current_user = request.user
    print current_user.id
# funcion login devuelve la vista login
def login(request):
    if request.method == 'POST':
        
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        print email,password
        user = authenticate(email=email, password=password)
        auth_login(request, user)
        return redirect('/dashboard/')
    else:
        sample_view(request)
        template = loader.get_template("login.html")
        contex = {
        'title': 'Agregar Cliente',
        
        }
        return HttpResponse(template.render(contex,request))

# funcion para registrar un nuevo cliente
def singin(request):
    if request.method == 'POST':
        form = Registrarme(request.POST, request.FILES)
        if form.is_valid():
            
            email = request.POST.get('correo', None)
            password = request.POST.get('password', None)
            print password
            is_personal = False
            user = MyUser.objects.create_user(email=email,is_personal=is_personal, password=password)
            user.save()
            usuario = form.save()
            usuario.save()
            return HttpResponseRedirect('/')
    else:
        form = Registrarme

    template = loader.get_template("singin.html")
    contex = {
        'title' : 'Registrarme',
        'form' : form
    }
    return HttpResponse(template.render(contex,request))
    

    """template = loader.get_template('singin.html')
    title = 'Registrarme'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))"""