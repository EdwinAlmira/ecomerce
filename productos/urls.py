from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^producto/(?P<pk>[0-9]+)/$', views.index, name='index'),
	url(r'^categorias/agregar',views.agregar_categoria, name ="agregar_categoria")
]
