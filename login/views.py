from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.template import loader
from django.views.decorators.csrf import csrf_exempt
from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from login.mixins import AdminAndPermisoRequiredMixin
# importa el modelo del cliente y el de autentifiacion(MyUser)
from cliente.models import Cliente
from login.models import MyUser , PersonalAdministrativo, Permiso, PermisoModulo, Modulo

# importa el formulario para registrar un cliente
from .forms import Registrarme, admin ,PermisosForm, AccessForm, Registrarme


# Vista generia para listar usuarios

class UsuariosList(AdminAndPermisoRequiredMixin,ListView):
    
    # definimos el modelo, template e intervalo de paginacion
    model = PersonalAdministrativo
    template_name = 'usuarios.html'
    paginate_by = 5

    # se sobreescribe el metodo para agregar la paginacion
    def get_context_data(self, **kwargs):
        #definimos el contexto al que tendra alcance la template
        context = super(UsuariosList, self).get_context_data(**kwargs) 
        # obtiene  los registros
        lista_usuarios = PersonalAdministrativo.objects.all()
        # obtiene el criterio de busqueda
        query = self.request.GET.get('q')

        if query:
            # si no esta vacia los filtra Q = LIKE en sql
            lista_usuarios = lista_usuarios.filter(
                Q(nombre__icontains=query)
                
                ).distinct()
        # obtiene la pagina para la paginacion
        page = self.request.GET.get('page')
        paginator = Paginator(lista_usuarios, self.paginate_by)
        try:
            lista_usuarios = paginator.page(page)
        except PageNotAnInteger:
            lista_usuarios = paginator.page(1)
        except EmptyPage:
            lista_usuarios = paginator.page(paginator.num_pages)

        # agrega la lista al contexto
        context['lista_usuarios'] = lista_usuarios
        return context

# Vista generica para crear un  usuario administrador
class UsuarioCreation(CreateView):
    form_class = admin
    template_name = 'agregar_usuario.html'
    model = PersonalAdministrativo
    success_url = '/dashboard/usuarios/'

# Vista generica para modificar un usuario administrador
class UsuarioUpdate(AdminAndPermisoRequiredMixin,UpdateView):
    form_class = admin
    template_name = 'modificar_usuario.html'
    model = PersonalAdministrativo
    success_url = '/dashboard/usuarios/'

# Vista generica para eliminar un nuevo usuario administrador
class UsuarioDelete(AdminAndPermisoRequiredMixin,DeleteView):
    model = PersonalAdministrativo
    template_name = 'confirmar.html'
    success_url = '/dashboard/usuarios/'

# Vista generia para listar usuarios

class PermisosList(AdminAndPermisoRequiredMixin ,ListView):
    
    # definimos el modelo, template e intervalo de paginacion
    model = Permiso
    template_name = 'permisos.html'
    paginate_by = 5

    # se sobreescribe el metodo para agregar la paginacion
    def get_context_data(self, **kwargs):
        #definimos el contexto al que tendra alcance la template
        context = super(PermisosList, self).get_context_data(**kwargs) 
        # obtiene  los registros
        lista_permisos = Permiso.objects.all()
        # obtiene el criterio de busqueda
        query = self.request.GET.get('q')

        if query:
            # si no esta vacia los filtra Q = LIKE en sql
            lista_permisos = lista_permisos.filter(
                Q(nombre__icontains=query)
                
                ).distinct()
        # obtiene la pagina para la paginacion
        page = self.request.GET.get('page')
        paginator = Paginator(lista_permisos, self.paginate_by)
        try:
            lista_permisos = paginator.page(page)
        except PageNotAnInteger:
            lista_permisos = paginator.page(1)
        except EmptyPage:
            lista_permisos = paginator.page(paginator.num_pages)

        # agrega la lista al contexto
        context['lista_permisos'] = lista_permisos
        return context

# Vista generica para crear un  permiso
class PermisoCreation(AdminAndPermisoRequiredMixin,CreateView):
    form_class = PermisosForm
    template_name = 'agregar_permiso.html'
    model = Permiso
    success_url = '/dashboard/permisos/'

# Vista generica para modificar un permiso
class PermisoUpdate(AdminAndPermisoRequiredMixin,UpdateView):
    form_class = PermisosForm
    template_name = 'modificar_permiso.html'
    model = Permiso
    success_url = '/dashboard/permisos/'

# Vista generica para eliminar un permiso
class PermisoDelete(AdminAndPermisoRequiredMixin,DeleteView):
    model = Permiso
    template_name = 'borrar_permiso.html'
    success_url = '/dashboard/permisos/'    

# Acceso listview
class AccesoList(AdminAndPermisoRequiredMixin,ListView):
    
    # definimos el modelo, template e intervalo de paginacion
    model = PermisoModulo
    template_name = 'acceso.html'
    paginate_by = 5

    # se sobreescribe el metodo para agregar la paginacion
    def get_context_data(self, **kwargs):
        #definimos el contexto al que tendra alcance la template
        context = super(AccesoList, self).get_context_data(**kwargs) 
        # obtiene  los registros
        modulos = PermisoModulo.objects.all()
        # obtiene el criterio de busqueda
        query = self.request.GET.get('q')

        if query:
            # si no esta vacia los filtra Q = LIKE en sql
            modulos = modulos.filter(
                Q(id_permiso=(Permiso.objects.get(nombre=query).pk)) 
                ).distinct()
        # obtiene la pagina para la paginacion
        page = self.request.GET.get('page')
        paginator = Paginator(modulos , self.paginate_by)
        try:
            modulos = paginator.page(page)
        except PageNotAnInteger:
            modulos = paginator.page(1)
        except EmptyPage:
            modulos = paginator.page(paginator.num_pages)

        # agrega la lista al contexto
        context['modulos'] = modulos
        return context

 # Vista generica para crear un  acceso
class AccesoCreation(AdminAndPermisoRequiredMixin,CreateView):
    form_class = AccessForm
    template_name = 'agregar_acceso.html'
    model = PermisoModulo
    success_url = '/dashboard/acceso/'     

class AccesoUpdate(AdminAndPermisoRequiredMixin,UpdateView):
    form_class = AccessForm
    template_name = 'modificar_acceso.html'
    model = PermisoModulo
    success_url = '/dashboard/acceso/'      

# Vista generica para eliminar un acceso
class AccesoDelete(AdminAndPermisoRequiredMixin,DeleteView):
    model = PermisoModulo
    template_name = 'borrar_acceso.html'
    success_url = '/dashboard/acceso/'    

# Vista generia para listar clientes

class ClientesList(AdminAndPermisoRequiredMixin,ListView):
    
    # definimos el modelo, template e intervalo de paginacion
    model = Cliente
    template_name = 'clientes.html'
    paginate_by = 5

    # se sobreescribe el metodo para agregar la paginacion
    def get_context_data(self, **kwargs):
        #definimos el contexto al que tendra alcance la template
        context = super(ClientesList, self).get_context_data(**kwargs) 
        # obtiene  los registros
        lista_clientes = Cliente.objects.all()
        # obtiene el criterio de busqueda
        query = self.request.GET.get('q')

        if query:
            # si no esta vacia los filtra Q = LIKE en sql
            lista_clientes = lista_clientes.filter(
                Q(nombre__icontains=query)
                
                ).distinct()
        # obtiene la pagina para la paginacion
        page = self.request.GET.get('page')
        paginator = Paginator(lista_clientes, self.paginate_by)
        try:
            lista_clientes = paginator.page(page)
        except PageNotAnInteger:
            lista_clientes = paginator.page(1)
        except EmptyPage:
            lista_clientes = paginator.page(paginator.num_pages)

        # agrega la lista al contexto
        context['lista_clientes'] = lista_clientes
        return context
class ClienteDetail(AdminAndPermisoRequiredMixin,DetailView):
    model = Cliente
    template_name = 'cliente_detalle.html'


def check_login_redirect(request):
    if request.user.is_authenticated():
        return True
    else:
        return False
# funcion para autentificar a los usuarios
def login(request):
    if check_login_redirect(request):
        return redirect('/dashboard/')
    if request.method == 'POST':

        #Obtiene la password y correo del usuario
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        #Intenta autentificarse con el modelo de MyUser
        user = authenticate(email=email, password=password)

        #una vez se verifica el usuario, inicia sesion
        auth_login(request, user)
        # redirecciona al dashboard, el cual identificara el tipo de usuario
        return redirect('/dashboard/')
    else:
        #Peticion para cargar la vista
        template = loader.get_template("login.html")
        contex = {
        'title': 'Iniciar Sesion',
        
        }
        return HttpResponse(template.render(contex,request))

# funcion para registrar un nuevo cliente
def singin(request):
    if request.method == 'POST':
        # Se crea un formulario y se rellena con el request
        form = Registrarme(request.POST, request.FILES)

        #se validan los datos del formulario
        if form.is_valid():
            
            #se obtiene el correo y contra para ser registrados en los usaurios
            email = request.POST.get('correo', None)
            password = request.POST.get('password', None)
            is_personal = False
            id_user = 0


            # se guarda el usuario tipo cliente en el modelo MyUser
            user = MyUser.objects.create_user(email=email,is_personal=is_personal, id_user=id_user, password=password)
            user.save()

            # se registra el cliente en el modelo cliente
            nuevo_cliente = form.save()
            nuevo_cliente.save()

             #Obtiene la password y correo del usuario
            new_user = authenticate(email=email, password=password)

            #una vez se verifica el usuario, inicia sesion
            auth_login(request, new_user)
            return HttpResponseRedirect('/login/')
    else:
        # peticion para la vista se obtiene el formulario
        form = Registrarme
    # se envia el formulario a la vista
    template = loader.get_template("singin.html")
    contex = {
        'title' : 'Registrarme',
        'form' : form
    }
    return HttpResponse(template.render(contex,request))