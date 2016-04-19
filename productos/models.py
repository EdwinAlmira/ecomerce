from __future__ import unicode_literals

from django.db import models

# categorias para los producros
class Categoria(models.Model):
	nombre = models.CharField(unique=True, max_length=50)
	def __str__(self):
		return self.nombre
# proveedores de los productos
class Proveedor(models.Model):
	nombre = models.CharField(max_length=50, null= False, unique=True)
	imagen = models.ImageField(blank = True, upload_to= 'img_proveedores', default = 'img_proveedores/no-img.jpg')
	def __str__(self):
		return self.nombre

# modelo productos
class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)
	descripcion = models.CharField(max_length=100)
	imagen = models.ImageField(blank = True, upload_to= 'img_productos', default = 'img_productos/no-img.jpg')
	id_proveedor = models.ForeignKey(Proveedor, models.DO_NOTHING)
	id_categoria = models.ForeignKey(Categoria, models.DO_NOTHING)

# alamcen lleva un inventario de los productos
class Almacen(models.Model):
    cantidad = models.IntegerField()
    vendidos = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    id_producto = models.ForeignKey(Producto, models.DO_NOTHING)