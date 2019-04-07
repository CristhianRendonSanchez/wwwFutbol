from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    # ayuda a django a trabajar con nuestro propio modelo de usuario
    def create_user(self, email, name, lastname, balance, dni, password=None):
        # crea un objeto como nuevo usuario

        if not email:
            raise ValueError("ingrese email")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name, lastname=lastname, balance=balance, dni=dni)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        # crea y guardar un nuevo usario administrador

        user = self.create_user(email, name,'', 0, 0, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Representa un perfil de usuario dentro de nuestro sistema.

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255, default='')
    lastname = models.CharField(max_length=255, default='')
    balance = models.IntegerField(default=0)
    dni = models.IntegerField(default=0)

    is_active = models.BooleanField(default=True)


    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    class Meta:
        db_table = "user_profile"

    def get_full_name(self):
        # usado para obtener el nombre completo
        return self.name

    def get_short_name(self):
        # usado para obtener el nombre corto
        return self.name

    def get_id(self):
        return self.id

    def __str__(self):
        # Djando usa esto cuando necesita convertir objecs a string
        return self.email

class Payoffs(models.Model):
    # modelo para gestion de recrgas
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    consigned_amount = models.IntegerField(default=0)
    date_amount = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "payoffs"

    def __str__(self):
        return self.user_id.__str__()



class Bets(models.Model):
    #modelo general de apuestas
    user_id = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    local_team = models.CharField(max_length=255)
    visiting_team = models.CharField(max_length=255)
    #id_match = models.IntegerField(default=0)
    league = models.CharField(max_length=255)
    balance = models.IntegerField(default=0)
    date = models.DateTimeField(null=True, blank=True)
    bets_state = models.BooleanField(default=False)

    class Meta:
        db_table = "bets"


class WinBets(models.Model):
    #modelo de apuestas por equpo ganador
    bets_id = models.ForeignKey(Bets, on_delete=models.CASCADE)
    team_bet = models.CharField(max_length=255)

    class Meta:
        db_table = "win_bets"

class MarkerBets(models.Model):
    #modelo de apuestas por marcador
    bets_id = models.ForeignKey(Bets, on_delete=models.CASCADE)
    local_marker = models.IntegerField(default=0)
    visiting_marker = models.IntegerField(default=0)

    class Meta:
        db_table = "marker_bets"

class GoalsBets(models.Model):
    bets_id = models.ForeignKey(Bets, on_delete=models.CASCADE)
    goals_dif = models.IntegerField(default=0)

    class Meta:
        db_table = "goals_bets"
