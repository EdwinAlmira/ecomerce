from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def login(request):
    template = loader.get_template('login.html')
    title = 'Iniciar Sesion'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))

def singin(request):
    template = loader.get_template('singin.html')
    title = 'Registrarme'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))