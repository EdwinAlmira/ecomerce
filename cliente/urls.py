from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^cliente/agregar', views.agregar_cliente, name='agregar_cliente'),
]