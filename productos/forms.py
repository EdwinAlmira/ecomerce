from django.forms import *
from .models import Categoria, Proveedor, Producto


class AgregarCategoria(ModelForm):
	class Meta:
		# definimos un modelo 
		model = Categoria
		# indicamos que tome todos los campos
		fields = '__all__'
		# definimos las propiedades de los campos al formulario
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombre'}),
	        }

class AgregarProveedor(ModelForm):
	class Meta:
		# definimos un modelo 
		model = Proveedor
		# indicamos que tome todos los campos
		fields = '__all__'
		# definimos las propiedades de los campos al formulario
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombre'}),
	        }	        

class AgregarProducto(ModelForm):
	class Meta:
		# definimos un modelo 
		model = Producto
		# indicamos que tome todos los campos
		fields = '__all__'
		# definimos las propiedades de los campos al formulario
		widgets = {
	            'nombre': TextInput(attrs={'class': 'form-control','placeholder':'Ingresa el nombre'}),
	        }	        