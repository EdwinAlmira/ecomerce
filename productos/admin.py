from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Categoria)
class AdminCategoria(admin.ModelAdmin):
	list_display = ('nombre',)
	
@admin.register(Proveedor)
class AdminProveedores(admin.ModelAdmin):
	list_display = ('nombre',)
