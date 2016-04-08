from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

def blog(request):
    template = loader.get_template('blog.html')
    title = 'Noticias'
    context = {
        'title': title
    }
    return HttpResponse(template.render(context, request))