from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

# se importan el modelo y el formulario

from cliente.models import Cliente
from .forms import Registrarme

# funcion login devuelve la vista login
def login(request):
    template = loader.get_template('login.html')
    title = 'Iniciar Sesion'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

# funcion para registrar un nuevo cliente
def singin(request):
    if request.method == 'POST':
        form = Registrarme(request.POST, request.FILES)
        if form.is_valid():
            cliente = form.save()
            cliente = save()
            return HttpResponseRedirect('/login')
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