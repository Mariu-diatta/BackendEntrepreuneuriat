from django.contrib import admin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db import models
from django.forms import Textarea
# Register your models here.
from .models  import User, CompteUser, Produit

class UserAdminConcfig(UserAdmin):
    model=User
    search_fields = ('mail','nom','prenom')
    list_filter = ('mail','prenom','is_active','is_staff')
    ordering = ('-start_date',)
    list_display = ('mail','nom','prenom','is_active','is_staff')
    fieldsets = [
        (None,               {'fields': ('mail','nom','prenom',)}),
        ('Permissions', {'fields': ('is_staff','is_active')}),
        ('Personal',{'fields':('about',)}),
        ('Mot de passe', {'fields': ('password',)}),
    ]

    formfield_overrides = {
        models.TextField:{'widget':Textarea(attrs={'rows':20,'cols':60})}
    }
    add_fieldsets = (
        (
            None,{
                'classes':('wide',),
                'fields':('user_email','user_first_name','user_last_name','password','is_active',)
            }
        )
    )
admin.site.register(User)
admin.site.register(CompteUser)
admin.site.register( Produit)