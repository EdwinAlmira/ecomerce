from __future__ import unicode_literals

from django.db import models
from cliente.models import Accion

class Modulo(models.Model):
	nombre = models.CharField(unique=True, max_length=50)

class Permiso(models.Model):
	nombre = models.CharField(unique=True, max_length=50)

class PermisoModulo(models.Model):
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)
	id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING)

class PersonalAdministrativo(models.Model):
	generos =(
		('M', 'Masculino'),
    	('F', 'Femenino')
    )	
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=9, blank=True, choices=generos)
	correo = models.CharField(unique=True, max_length=60)
	telefono = models.CharField(unique=True, max_length=10)
	nacimiento = models.DateField()
	contra = models.CharField(max_length=120)
	foto = models.ImageField(blank = True, upload_to= 'img_personal', default = 'img_personal/no-img.jpg')
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)

class Bitacora(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	descripcion = models.CharField(max_length=100)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	id_personal = models.ForeignKey(PersonalAdministrativo, models.DO_NOTHING)
