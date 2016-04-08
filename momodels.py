# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Acciones(models.Model):
    id_accion = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'acciones'


class Almacen(models.Model):
    id_almacen = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    vendidos = models.IntegerField()
    fecha_ingreso = models.DateTimeField()
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')

    class Meta:
        managed = False
        db_table = 'almacen'


class Bitacora(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    fecha = models.DateField()
    hora = models.TimeField()
    descripcion = models.CharField(max_length=100)
    id_accion = models.ForeignKey(Acciones, models.DO_NOTHING, db_column='id_accion')
    id_personal = models.ForeignKey('PersonalAdministrativo', models.DO_NOTHING, db_column='id_personal')

    class Meta:
        managed = False
        db_table = 'bitacora'


class BitacoraCliente(models.Model):
    id_bitacora = models.AutoField(primary_key=True)
    fecha = models.DateField()
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente')
    id_accion = models.ForeignKey(Acciones, models.DO_NOTHING, db_column='id_accion')

    class Meta:
        managed = False
        db_table = 'bitacora_cliente'


class Calaficiaciones(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    estrellas = models.DecimalField(max_digits=2, decimal_places=1)
    fecha = models.DateTimeField()
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'calaficiaciones'


class Carrito(models.Model):
    id_carrito = models.AutoField(primary_key=True)
    cantidad = models.IntegerField()
    estado = models.IntegerField()
    fecha = models.DateField()
    hora = models.TimeField()
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_cliente = models.ForeignKey('Clientes', models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'carrito'


class Categorias(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'categorias'


class Clientes(models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=9, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=60)
    telefono = models.CharField(unique=True, max_length=10)
    pass_field = models.CharField(db_column='pass', max_length=120)  # Field renamed because it was a Python reserved word.
    ingreso = models.DateField()
    estado = models.CharField(max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clientes'


class Comentarios(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    comentario = models.CharField(max_length=150)
    fecha = models.DateTimeField()
    estado = models.CharField(max_length=9, blank=True, null=True)
    id_producto = models.ForeignKey('Productos', models.DO_NOTHING, db_column='id_producto')
    id_cliente = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='id_cliente')

    class Meta:
        managed = False
        db_table = 'comentarios'


class Factura(models.Model):
    id_factura = models.AutoField(primary_key=True)
    monto = models.DecimalField(max_digits=6, decimal_places=2)
    fecha = models.DateTimeField()
    id_carrito = models.ForeignKey(Carrito, models.DO_NOTHING, db_column='id_carrito')

    class Meta:
        managed = False
        db_table = 'factura'


class Modulos(models.Model):
    id_modulo = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'modulos'


class Permisos(models.Model):
    id_permiso = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'permisos'


class PermisosModulos(models.Model):
    id_permiso_modulo = models.AutoField(primary_key=True)
    id_permiso = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='id_permiso')
    id_modulo = models.ForeignKey(Modulos, models.DO_NOTHING, db_column='id_modulo')

    class Meta:
        managed = False
        db_table = 'permisos_modulos'


class PersonalAdministrativo(models.Model):
    id_personal = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    genero = models.CharField(max_length=9, blank=True, null=True)
    correo = models.CharField(unique=True, max_length=60)
    telefono = models.CharField(unique=True, max_length=10)
    nacimiento = models.DateField()
    pass_field = models.CharField(db_column='pass', max_length=120)  # Field renamed because it was a Python reserved word.
    foto = models.CharField(max_length=100)
    id_permiso = models.ForeignKey(Permisos, models.DO_NOTHING, db_column='id_permiso')

    class Meta:
        managed = False
        db_table = 'personal_administrativo'


class Productos(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    precio_unitario = models.DecimalField(max_digits=6, decimal_places=2)
    descripcion = models.CharField(max_length=100)
    imagen = models.CharField(max_length=60)
    id_proveedor = models.ForeignKey('Proveedores', models.DO_NOTHING, db_column='id_proveedor')
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')

    class Meta:
        managed = False
        db_table = 'productos'


class Proveedores(models.Model):
    id_proveedor = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'proveedores'
