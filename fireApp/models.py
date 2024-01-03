from django.db import models


# Create your models here.
class User(models.Model):
    date_add = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    imageProfile = models.ImageField(upload_to='product')
    genre = models.CharField(max_length=255)
    ville = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    isRegistered = models.CharField(max_length=255)

    def __unicode__(self):
        return "{0}".format(self.password, )


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
