from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^producto/(?P<pk>[0-9]+)/$', views.index, name='index'),
	url(r'^categorias/agregar',views.agregar_categoria, name ="agregar_categoria"),
	url(r'^proveedores/agregar',views.agregar_proveedor, name ="agregar_proveedor"),
	url(r'^producto/agregar',views.agregar_producto, name ="agregar_producto"),
]
