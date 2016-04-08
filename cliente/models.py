from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from productos.models import Producto 

class Cliente(models.Model):

	estados =(
		('on','Activo'),
		('off','Inactivo')
	)
	generos =(
		('M', 'Masculino'),
    	('F', 'Femenino')
    )

	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=9, blank=True, choices=generos, default = 'M')
	correo = models.CharField(unique=True, max_length=60)
	telefono = models.CharField(unique=True, max_length=10)
	contra = models.CharField(max_length=120)
	ingreso = models.DateField(auto_now_add = True, blank= True)
	estado = models.CharField(max_length=8, blank=False, choices=estados, default = 'on')

class Accion(models.Model):
	acciones =(
		('save','Guardardo'),
		('update','Modifico'),
		('delete','Elimino'),
		('buy','Compro'),
		('check','Consulto')
	)
	nombre = models.CharField(unique=True, max_length=50, choices=acciones)


class BitacoraCliente(models.Model):
	fecha = models.DateField()
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	descripcion = models.CharField(max_length=100)

class Calaficiacion(models.Model):
	estrellas = models.DecimalField(max_digits=2, decimal_places=1)
	fecha = models.DateTimeField()
	id_producto = models.ForeignKey(Producto, models.DO_NOTHING)
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

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
