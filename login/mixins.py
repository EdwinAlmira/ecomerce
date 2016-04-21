from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.http import HttpResponseRedirect

from login.models import MyUser, PersonalAdministrativo, Permiso, PermisoModulo

# Mixin para verificar que el usuario sea administrador y qe tenga permisos para realizar la accion
class AdminAndPermisoRequiredMixin(object):
	# requiere un login
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
    	# obtiene el usuario apartir del email
    	email = request.user
    	user = MyUser.objects.get(email=email)
    	if not user.is_personal:
            return redirect('/login/')
        else:
        	print request.path
        	return super(AdminAndPermisoRequiredMixin, self).dispatch(request, *args, **kwargs)
