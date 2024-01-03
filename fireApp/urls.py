from django.urls import path
from .views import User, Produit, CompteUser

urlpatterns = [
    path('users', User.as_view(), name='users'),
    path('comptesUsers', CompteUser.as_view(), name='comptes users'),
    path('produitsUsers', Produit.as_view(), name='produits users')
]