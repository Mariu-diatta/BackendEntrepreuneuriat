from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea
# Register your models here.
from .models  import User, CompteUser, Produit
admin.site.register(User)
admin.site.register(CompteUser)
admin.site.register( Produit)