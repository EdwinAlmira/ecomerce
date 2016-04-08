from django import forms
from .models import Cliente

class AgregarCliente(forms.ModelForm):
	class Meta:
		model= Cliente
		fields = '__all__'
