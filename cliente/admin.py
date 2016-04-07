from django.contrib import admin
from .models import *

# Register your models here.
#another comment 

@admin.register(Cliente)
class AdminCliente(admin.ModelAdmin):
	list_display = ('nombre','genero',)