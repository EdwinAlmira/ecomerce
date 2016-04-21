from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/', views.login, name='login'),
    url(r'^singin/', views.singin, name='singin'),
    url(r'^dashboard/usuarios/',views.UsuariosList.as_view(), name ="UsuariosList"),
	url(r'^dashboard/usuario/agregar/', views.UsuarioCreation.as_view(), name="UsuarioCreation"),
	url(r'^dashboard/usuario/modificar/(?P<pk>\d+)$', views.UsuarioUpdate.as_view(), name="edit_usuario"),
	url(r'^dashboard/usuario/borrar/(?P<pk>\d+)$', views.UsuarioDelete.as_view(), name = 'delete_usuario'),
	url(r'^dashboard/permisos/',views.PermisosList.as_view(), name ="PermisosList"),
	url(r'^dashboard/permiso/agregar/', views.PermisoCreation.as_view(), name="PermisoCreation"),
	url(r'^dashboard/permiso/modificar/(?P<pk>\d+)$', views.PermisoUpdate.as_view(), name="edit_permiso"),
	url(r'^dashboard/permiso/borrar/(?P<pk>\d+)$', views.PermisoDelete.as_view(), name="delete_permiso"),
	url(r'^dashboard/acceso/',views.AccesoList.as_view(), name ="AccesoList"),
	url(r'^dashboard/accesos/agregar/', views.AccesoCreation.as_view(), name="AccesoCreation"),
	url(r'^dashboard/accesos/modificar/(?P<pk>\d+)$', views.AccesoUpdate.as_view(), name="edit_acceso"),
	url(r'^dashboard/accesos/borrar/(?P<pk>\d+)$', views.AccesoDelete.as_view(), name="delete_acceso"),
	url(r'^dashboard/clientes/',views.ClientesList.as_view(), name ="ClientesList"),
	url(r'^dashboard/cliente/detalle/(?P<pk>\d+)$', views.ClienteDetail.as_view(), name="detalle_cliente"),
	
]