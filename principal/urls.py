from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^productos/', views.productos, name='productos'),
	url(r'^compra/', views.compra, name='compra'),
	url(r'^conocenos/', views.conocenos, name='conocenos'),
	url(r'^preguntas/', views.preguntas, name='preguntas'),
]