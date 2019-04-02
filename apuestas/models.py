from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    #ayuda a django a trabajar con nuestro propio modelo de usuario
    def create_user(self, email, name, lastname, balance, dni, password=None):
        #crea un objeto como nuevo usuario

        if not email:
            raise ValueError("ingrese email")

        email =self.normalize_email(email)
        user = self.model(email=email, name=name, lastname=lastname, balance=balance, dni=dni)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        #crea y guardar un nuevo usario administrador

        user = self.create_user(email, name, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    #Representa un perfil de usuario dentro de nuestro sistema.

    email = models.EmailField(max_length=255, unique=True, primary_key= True)
    name = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    balance = models.IntegerField(default=0)
    dni = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
       # usado para obtener el nombre completo
        return self.name

    def get_short_name(self):
        #usado para obtener el nombre corto
        return self.name

    def get_id(self):
        return self.id


    def __str__(self):
        #Djando usa esto cuando necesita convertir objecs a string
        return self.email



class Balance(models.Model):
    #modelo para gestion de recrgas
    consigned_amount = models.IntegerField(default=0)
    date_amount = models.DateTimeField(null=True, blank=True)
    user_id = models.ForeignKey(UserProfile.dni, on_delete=models.CASCADE)

    def NewBalance(self, amount, date, user):
        balance = self.model(consigned_amount=amount, date_amount=date, user_id=user)
        #funcion que actulizce el saldo del usuario
        balance.save(using=self._db)


    def __str__(self):
        return self.consigned_amount()


