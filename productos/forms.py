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
				'imagen': FileInput(attrs={'class':'form-control upload',}),
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
	            'precio_unitario': NumberInput(attrs={'class': 'form-control','placeholder':'9.99'}),
	            'imagen': FileInput(attrs={'class':'form-control upload',}),
	            'id_proveedor': Select(attrs={'class': 'form-control'}),
	            'id_categoria': Select(attrs={'class': 'form-control'}),
	            'descripcion': Textarea(attrs={'class': 'form-control'}),
	        }	        