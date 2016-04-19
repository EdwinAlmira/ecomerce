from __future__ import unicode_literals
from django.db import models
from cliente.models import Accion, Cliente

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class MyUserManager(BaseUserManager):
    def create_user(self, email, is_personal, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            is_personal=is_personal,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, is_personal, password):
        user = self.create_user(email,
            password=password,
            is_personal=is_personal
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_personal = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    objects = MyUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['is_personal']

    def get_full_name(self):
        # The user is identified by their email address 
        return self.email
    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True
    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
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
	foto = models.ImageField(blank = True, upload_to= 'img_personal', default = 'img_personal/no-img.jpg')
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)

class Bitacora(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	descripcion = models.CharField(max_length=100)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	id_personal = models.ForeignKey(PersonalAdministrativo, models.DO_NOTHING)
