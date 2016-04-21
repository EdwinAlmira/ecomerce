from django.forms import *

# importamos el modelo del cliente
from cliente.models import Cliente
from .models import  PersonalAdministrativo, Permiso, PermisoModulo 

# formulario para registrar un nuevo cliente
class Registrarme(ModelForm):
	class Meta:
		# definimos un modelo 
		model = Cliente
		# indicamos que tome todos los campos
		fields = '__all__'
		# definimos las propiedades de los campos al formulario
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa su nombres'}),
	            'apellido': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese sus apellidos','id':'lname'}),
	            'correo' : EmailInput(attrs={'name':'email','class': 'form-control','placeholder':'Ingrese su correo electronico','id':'email'}),
				'genero': Select(attrs={'class': 'form-control'}),
				'telefono': TextInput(attrs={'class': 'form-control','placeholder':'0000-0000','id':'telefono'}),
				'estado': Select(attrs={'class': 'invisible'}),            
	        }

# formulario acceso

class AccessForm(ModelForm):
	class Meta:
		model = PermisoModulo
		fields = '__all__'
		widgets={
			'id_permiso': Select(attrs={'class': 'form-control'}),
			'id_modulo': Select(attrs={'class': 'form-control'}), 
		}

# formulario para los permisos	        
class PermisosForm(ModelForm):
	class Meta:
		model = Permiso
		fields = '__all__'
		widgets={
			'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombres'}),
		}
# formulario para  admin
class admin(ModelForm):
	class Meta:	
		# definimos un modelo 
		model = PersonalAdministrativo
		# indicamos que tome todos los campos
		fields = '__all__'
		# definimos las propiedades de los campos al formulario
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa su nombres'}),
	            'apellido': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese sus apellidos','id':'lname'}),
	            'correo' : EmailInput(attrs={'name':'email','class': 'form-control','placeholder':'Ingrese su correo electronico','id':'email'}),
				'genero': Select(attrs={'class': 'form-control'}),
				'telefono': TextInput(attrs={'class': 'form-control','placeholder':'0000-0000','id':'telefono'}),
				'nacimiento': TextInput(attrs={'class': 'form-control','placeholder':'1998-08-28','id':'permiso'}),
				'id_permiso': Select(attrs={'class': 'form-control'}),            
				'contra': PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese la clave','id':'contra'}),
				'foto': FileInput(attrs={'class':'form-control upload',}),
	        }	        