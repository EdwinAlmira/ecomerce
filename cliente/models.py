from __future__ import unicode_literals
from datetime import datetime

from django.db import models
# importa el modelo del producto
from productos.models import Producto 

# Modelo Cliente
class Cliente(models.Model):

# tupla para controlar los estados y generos	
	estados =(
		('on','Activo'),
		('off','Inactivo')
	)
	generos =(
		('M', 'Masculino'),
    	('F', 'Femenino')
    )
# Campos del modelo del Cliente
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=9, blank=True, choices=generos, default = 'M')
	correo = models.CharField(unique=True, max_length=60)
	telefono = models.CharField(unique=True, max_length=10)
	ingreso = models.DateField(auto_now_add = True, blank= True)
	estado = models.CharField(max_length=8, blank=False, choices=estados, default = 'on')

# Modelo accion para guardarlo en las bitacoras
class Accion(models.Model):
	acciones =(
		('save','Guardardo'),
		('update','Modifico'),
		('delete','Elimino'),
		('buy','Compro'),
		('check','Consulto')
	)
	nombre = models.CharField(unique=True, max_length=50, choices=acciones)

# Modelo para almacenar todas las acciones que el cliente realiza en la plataforma
class BitacoraCliente(models.Model):
	fecha = models.DateField()
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	descripcion = models.CharField(max_length=100)

# Modelo para calificar productos 
class Calaficiacion(models.Model):
	estrellas = models.DecimalField(max_digits=2, decimal_places=1)
	fecha = models.DateTimeField()
	id_producto = models.ForeignKey(Producto, models.DO_NOTHING)
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

# Modelo para los comentarios emitidos a los productos
class Comentario(models.Model):
	estados =(
		('show','Aceptado'),
		('hide','Rechado')
	)
	comentario = models.CharField(max_length=150)
	fecha = models.DateTimeField()
	estado = models.CharField(max_length=9, blank=True, choices=estados)
	id_producto = models.ForeignKey(Producto, models.DO_NOTHING)
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
