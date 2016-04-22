from __future__ import unicode_literals
from django.db import models
from cliente.models import Accion, Cliente
from django.db import models
from django.db.models import signals

#Importamos los siguientes modelos para poder realizar nuestro CustomUserModel
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)

# callback se ejecuta depues de modificar o guardar un usuario
def create_newadmin(sender, instance, created, **kwargs):
    # instance contiene una instancia del modelo    

    # obtenemos los datos del registro
    correo = sender.objects.get(pk=instance.pk).correo
    contra = sender.objects.get(pk=instance.pk).contra
    id_user = sender.objects.get(pk=instance.pk).id
    is_personal = True

    # intentamos selecionar el usuario
    try:
        user = MyUser.objects.get(id_user=id_user)
    except:
            # si no existe se guarda el usuario en el modelo MyUser
            user = MyUser.objects.create_user(
                email=correo,
                is_personal=is_personal,
                id_user = id_user,
                password=contra
                )
            user.save()
         

# Administrador de usuarios del sistema
class MyUserManager(BaseUserManager):
    # crear un usuario
    def create_user(self, email, is_personal,id_user , password=None):
        #validadcion del email
        if not email:
            raise ValueError('Usuario deben tener un correo')
        user = self.model(
            email=self.normalize_email(email),
            is_personal=is_personal,
            id_user=id_user
        )
        # ecripta la contra
        user.set_password(password)
        user.save(using=self._db)
        return user
    # funcion pra crear usuario disponibles en el admin
    def create_superuser(self, email, is_personal,id_user, password):
        user = self.create_user(email,
            password=password,
            is_personal=is_personal,
            id_user=id_user
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
    id_user= models.CharField( max_length=120, default = '0')
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
        def __str__(self):
            return self.nombre

# Permisos para ser asignados al personal
class Permiso(models.Model):
	nombre = models.CharField(unique=True, max_length=50)
        def __str__(self):
            return self.nombre

# Relacion permiso y sus modulos disponibles
class PermisoModulo(models.Model):
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)
	id_modulo = models.ForeignKey(Modulo, models.DO_NOTHING)

# Modelo personal administrativo 
class PersonalAdministrativo(models.Model):

        contra = models.CharField( max_length=120, default = 'rudeware')
	generos =(
		('M', 'Masculino'),
    	('F', 'Femenino')
    )	
	nombre = models.CharField(max_length=50)
	apellido = models.CharField(max_length=50)
	genero = models.CharField(max_length=9, blank=True, choices=generos, default = 'M')
	correo = models.CharField(unique=True, max_length=60)
	telefono = models.CharField(unique=True, max_length=10)
	nacimiento = models.DateField()
	foto = models.ImageField(blank = True, upload_to= 'img_personal', default = 'img_personal/no-img.jpg')
	id_permiso = models.ForeignKey(Permiso, models.DO_NOTHING)

        def __str__(self):
            return self.nombre +" "+ self.apellido

# relacionamos las acciones en el Modelo con el callback
signals.post_save.connect(create_newadmin, sender=PersonalAdministrativo)  

# Bitacora para todas las acciones dentro del sistema
class Bitacora(models.Model):
	fecha = models.DateField()
	hora = models.TimeField()
	descripcion = models.CharField(max_length=100)
	id_accion = models.ForeignKey(Accion, models.DO_NOTHING)
	id_personal = models.ForeignKey(PersonalAdministrativo, models.DO_NOTHING)
