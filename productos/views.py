from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

# modelos y su respectivo formulario
from .models import Categoria, Proveedor, Producto
from .forms	import AgregarCategoria, AgregarProveedor, AgregarProducto

from login.mixins import AdminAndPermisoRequiredMixin
# aceptar peticion sin token
@csrf_exempt
def update(request, pk):
	categoria = Categoria.objects.get(pk=pk)
	form = AgregarCategoria(request.POST or None, instance=categoria)
	if form.is_valid():
		form.save()
		return redirect('/dashboard/categorias')

# eliminar categoria
def delete(request, pk):
	Categoria.objects.get(id=pk).delete()
	return HttpResponseRedirect('/dashboard/categorias')


# funcion agregar categoria
def categorias(request):
	# verifica que el usuario este logeado
	if not request.user.is_authenticated():
		return redirect('/login/')

	user = request.user
	# si intenta guardarlo
	if request.method == 'POST':
		form = AgregarCategoria(request.POST)
		if form.is_valid():
			categoria = form.save()
			categoria.save()
		return HttpResponseRedirect('/dashboard/categorias')
	# si el usuario admin intenta obtener la vista
	elif user.is_personal:
		form = AgregarCategoria()
		categorias_lista = Categoria.objects.all()
		paginator = Paginator(categorias_lista, 5)
		page = request.GET.get('page')
		try:
			categorias = paginator.page(page)
		except PageNotAnInteger:
			# If page is not an integer, deliver first page.
			categorias = paginator.page(1)
		except EmptyPage:
			# If page is out of range (e.g. 9999), deliver last page of results.
			categorias = paginator.page(paginator.num_pages)

		template = loader.get_template("agregar_categoria.html")
		contex = {
			'form': form,
			'categorias': categorias,
			'paginator': paginator,
		}
		return HttpResponse(template.render(contex,request))

	#si el usuario no es del personal administrativo	
	return HttpResponseRedirect('/dashboard/')		

# funcion agregar producto
def agregar_producto(request):
	# verifica que el usuario este logeado
	if not request.user.is_authenticated():
		return redirect('/login/')

	user = request.user
	# si intenta guardarlo
	if request.method == 'POST':
		form = AgregarProducto(request.POST, request.FILES)
		if form.is_valid():
			producto = form.save()
			producto.save()
			
		return HttpResponseRedirect('/dashboard/')
	# si el usuario admin intenta obtener la vista
	elif user.is_personal:
		form = AgregarProducto()
		template = loader.get_template("agregar_producto.html")
		contex = {
			'form': form
		}
		return HttpResponse(template.render(contex,request))

	#si el usuario no es del personal administrativo	
	return HttpResponseRedirect('/dashboard/')

# ListViews para los Proveedores
class ProveedoresList(AdminAndPermisoRequiredMixin,ListView):
	# define el modelo
	model = Proveedor
	template_name = 'proveedores.html'
	paginate_by = 5

	# sobreescribe el contexto
	def get_context_data(self, **kwargs):
		context = super(ProveedoresList, self).get_context_data(**kwargs) 
		lista_proveedores = Proveedor.objects.all()
		page = self.request.GET.get('page')
		query = self.request.GET.get('q')
		if query:
			# si hay un perametro de busca lo filta
			lista_proveedores = lista_proveedores.filter(
				Q(nombre__icontains=query)
				)

		paginator = Paginator(lista_proveedores, self.paginate_by)

		try:
			proveedores_list = paginator.page(page)
		except PageNotAnInteger:
			proveedores_list = paginator.page(1)
		except EmptyPage:
			proveedores_list = paginator.page(paginator.num_pages)

		# agrega los datos al contexto
		context['proveedores_list'] = proveedores_list
		return context

# muestra los detalles de los proveedores
class ProveedoresDetail(AdminAndPermisoRequiredMixin,DetailView):
	model = Proveedor

# generic view para agregar un proveedor
class ProveedoresCreation(AdminAndPermisoRequiredMixin,CreateView):
	form_class = AgregarProveedor
	template_name = 'agregar_proveedor.html'
	model = Proveedor
	success_url = '/dashboard/proveedores'

# generic view para editar un proveedor
class ProveedoresUpdate(AdminAndPermisoRequiredMixin,UpdateView):
	form_class = AgregarProveedor
	template_name = 'modificar_proveedor.html'
	model = Proveedor
	success_url = '/dashboard/proveedores'

# generic view para eliminar un proveedor
class ProveedoresDelete(AdminAndPermisoRequiredMixin,DeleteView):
	model = Proveedor
	template_name = 'confirmar.html'
	success_url = '/dashboard/proveedores'


# ListViews para los productos

class ProductosList(AdminAndPermisoRequiredMixin,ListView):
	model = Producto
	template_name = 'admin_productos.html'
	paginate_by = 5

	def get_context_data(self, **kwargs):
		context = super(ProductosList, self).get_context_data(**kwargs) 
		lista_prodcutos = Producto.objects.all()
		query = self.request.GET.get('q')
		if query:
			# genera la busqueda
			lista_prodcutos = lista_prodcutos.filter(
				Q(nombre__icontains=query)|
				Q(precio_unitario__icontains=query) 
				
				).distinct()

		page = self.request.GET.get('page')
		paginator = Paginator(lista_prodcutos, self.paginate_by)
		try:
			producto_list = paginator.page(page)
		except PageNotAnInteger:
			producto_list = paginator.page(1)
		except EmptyPage:
			producto_list = paginator.page(paginator.num_pages)
		# agrega el contexto
		context['producto_list'] = producto_list
		return context

# generic view para crear un producto
class ProductoCreation(AdminAndPermisoRequiredMixin,CreateView):
	form_class = AgregarProducto
	template_name = 'agregar_producto.html'
	model = Producto
	success_url = '/dashboard/productos'

# generic view para editar un producto
class ProductoUpdate(AdminAndPermisoRequiredMixin,UpdateView):
	form_class = AgregarProducto
	template_name = 'modificar_producto.html'
	model = Producto
	success_url = '/dashboard/productos'

# generic view para eliminar un producto
class ProductoDelete(AdminAndPermisoRequiredMixin,DeleteView):
	template_name = 'borrar_producto.html'
	model = Producto
	success_url = '/dashboard/productos'