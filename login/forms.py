from django.forms import *

# importamos el modelo del cliente
from cliente.models import Cliente

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