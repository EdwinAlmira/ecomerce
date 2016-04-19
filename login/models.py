from __future__ import unicode_literals
from django.db import models
from cliente.models import Accion, Cliente
from django.db import models

#Importamos los siguientes modelos para poder realizar nuestro CustomUserModel
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# Administrador de usuarios del sistema
class MyUserManager(BaseUserManager):
    # crear un usuario
    def create_user(self, email, is_personal, password=None):
        #validadcion del email
        if not email:
            raise ValueError('Usuario deben tener un correo')
        user = self.model(
            email=self.normalize_email(email),
            is_personal=is_personal,
        )
        # ecripta la contra
        user.set_password(password)
        user.save(using=self._db)
        return user
    # funcion pra crear usuario disponibles en el admin
    def create_superuser(self, email, is_personal, password):
        user = self.create_user(email,
            password=password,
            is_personal=is_personal
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

# Modelo por default para el manejo de usuario y autentificacion de usuarios
class MyUser(AbstractBaseUser):
    # definimos los campos del modelo
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_personal = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()
    # username sera remplazado por el correo
    USERNAME_FIELD = 'email'
    # es obligatorio indicar el tipo de usuario
    REQUIRED_FIELDS = ['is_personal']

    def get_full_name(self):
     
        return self.email
    def get_short_name(self):
     
        return self.email

    def __str__(self):
        return self.email
   
# Modulo para almacenar todas las funciones del sistema   
class Modulo(models.Model):
	nombre = models.CharField(unique=True, max_length=50)

# Permisos para ser asignados al personal
class Permiso(models.Model):
	nombre = models.CharField(unique=True, max_length=50)

# Relacion permiso y sus modulos disponibles
class PermisoModulo(models.Model):
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)
	id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING)

# Modelo personal administrativo 
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
	foto = models.ImageField(blank = True, upload_to= 'img_personal', default = 'img_personal/no-img.jpg')
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)

# Bitacora para todas las acciones dentro del sistema
class Bitacora(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	descripcion = models.CharField(max_length=100)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	id_personal = models.ForeignKey(PersonalAdministrativo, models.DO_NOTHING)
