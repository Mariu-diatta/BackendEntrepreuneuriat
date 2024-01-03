from datetime import timezone

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken


class CustomAccountManager(BaseUserManager):
    def create_superuser(self, nom, prenom, mail, tel, password, **other_fields):
        other_fields.setdefault('is_staff', False)
        other_fields.setdefault('is_superuser', False)
        other_fields.setdefault('is_active', False)
        if other_fields.get('is_staff') is not True:
            if other_fields.get('is_superuser') is not True:
                raise ValueError('Superuser must be assigned to is_superuser=True.')
            return self.create_user(nom, prenom, mail, tel, password, **other_fields)

        def create_user(self, nom, prenom, mail, tel, password, **other_fields):
            if not mail:
                raise ValueError('You must provide an email address')
                mail = self.normalize_email(mail)
            user = self.model(nom=nom, prenom=prenom, mail=mail,
                              tel=tel, password=password, **other_fields)
            user.set_password(password)
            user.save()
            return user


# Create your models here.
class User(AbstractBaseUser,PermissionsMixin):
    date_add = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    imageProfile = models.FileField(upload_to='profile/%Y/%m/%d/')
    genre = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    mail = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'mail'
    REQUIRED_FIELDS = ['nom', 'prenom', 'tel']
    objects = CustomAccountManager()

    def __str__(self):
        return self.mail

    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)

        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }


class CompteUser(models.Model):
    user_code = models.ForeignKey('User', null=False, on_delete=models.CASCADE, )
    date_add = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "{0}".format(self.user_code, )


class Produit(models.Model):
    produit_compte = models.ForeignKey('CompteUser', null=False, on_delete=models.CASCADE, )
    date_add = models.DateTimeField(auto_now_add=True)
    produit_image = models.ImageField(upload_to='product')

    def __unicode__(self):
        return "{0}".format(self.produit_compte, )
