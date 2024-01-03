from rest_framework import serializers
from fireApp.models import User, Produit, CompteUser


class ProduittSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produit
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class CompteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompteUser
        fields = "__all__"
