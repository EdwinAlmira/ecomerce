from django.contrib import admin
from .models import *

# Registrar los modelos en el admin

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre','genero',)