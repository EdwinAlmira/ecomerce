from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^dashboard/categoria/borrar/(?P<pk>[0-9]+)/$', views.delete, name ="delete_categoria"),
	url(r'^dashboard/categoria/editar/(?P<pk>[0-9]+)/$', views.update, name="edit_categoria"),
	url(r'^dashboard/categorias',views.categorias, name ="categorias"),
	url(r'^dashboard/proveedores/agregar',views.ProveedoresCreation.as_view(), name="agregar_proveedores"),
	url(r'^dashboard/proveedores/modificar/(?P<pk>\d+)$',views.ProveedoresUpdate.as_view(), name="editproveedor"),
	url(r'^dashboard/proveedores/borrar/(?P<pk>\d+)$', views.ProveedoresDelete.as_view(), name = 'delete_proveedor'),
	url(r'^dashboard/proveedores',views.ProveedoresList.as_view(), name="proveedores"),
	url(r'^dashboard/productos',views.ProductosList.as_view(), name ="listaproducto"),
	url(r'^dashboard/producto/agregar',views.ProductoCreation.as_view(), name="agregar_producto"),
	url(r'^dashboard/producto/modificar/(?P<pk>\d+)$',views.ProductoUpdate.as_view(), name="editproducto"),
	url(r'^dashboard/producto/borrar/(?P<pk>\d+)$', views.ProductoDelete.as_view(), name = "deleteproducto"),
]
