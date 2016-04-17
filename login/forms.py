from django.forms import *
from cliente.models import Cliente

class Registrarme(ModelForm):
	class Meta:
		model = Cliente
		fields = '__all__'
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa su nombres'}),
	            'apellido': TextInput(attrs={'class': 'form-control','placeholder':'Ingrese sus apellidos','id':'lname'}),
	            'correo' : EmailInput(attrs={'class': 'form-control','placeholder':'Ingrese su correo electronico','id':'email'}),
				'contra': PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','id':'pwd'}),            
				'genero': Select(attrs={'class': 'form-control'}),
				'telefono': TextInput(attrs={'class': 'form-control','placeholder':'0000-0000','id':'telefono'}),
				'estado': Select(attrs={'class': 'invisible'}),            
	        }