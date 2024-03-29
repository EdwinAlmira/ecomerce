from __future__ import unicode_literals
from django.db import models

# importa los modelos de clientes y productos
from cliente.models import Cliente
from productos.models import Producto

# Modelo donde se agrega los productos que el cliente desea adquirir
class Carrito(models.Model):
	estados =(
		('done','Realizado'),
		('off','Cancelado'),
		('on','Pendiente')
	)
	cantidad = models.IntegerField()
	estado = models.IntegerField(choices=estados)
	fecha = models.DateField()
	hora = models.TimeField()
	id_producto = models.ForeignKey(Producto, models.DO_NOTHING)
	id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING)

# facturacion del cliente
class Factura(models.Model):
	monto = models.DecimalField(max_digits=6, decimal_places=2)
	fecha = models.DateTimeField()
	id_carrito = models.ForeignKey(Carrito, models.DO_NOTHING)

