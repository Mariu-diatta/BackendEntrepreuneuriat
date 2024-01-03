from rest_framework import viewsets, routers, generics
from rest_framework.views import APIView

from fireApp.models import Produit, User, CompteUser
from my_fire_app.serializers import ProduittSerializer, UserSerializer, CompteSerializer


class Produit(generics.ListAPIView):
    queryset = Produit.objects.all()
    serializer_class =ProduittSerializer

class User(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CompteUser(generics.ListAPIView):
    queryset = CompteUser.objects.all()
    serializer_class = CompteSerializer

