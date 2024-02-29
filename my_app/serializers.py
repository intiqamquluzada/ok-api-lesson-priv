from rest_framework import serializers
from my_app.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class IndexSerializer(serializers.ModelSerializer):
    class Meta:
        model = Index
        fields = "__all__"

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"

class BlogSeializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"

class ContactSrializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = "__all__"

class MainDetailsserializer(serializers.ModelSerializer):
    class Meta:
        model = MainDetails
        fields = "__all__"

class SosialMediaserializer(serializers.ModelSerializer):
    class Meta:
        model = SosialMedia
        fields = "__all__"

class Askserializer(serializers.ModelSerializer):
    class Meta:
        model = Ask
        fields = "__all__" 

class Modelserializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = "__all__"

class Markaseializer(serializers.ModelSerializer):
    class Meta:
        model = Marka
        fields = "__all__"

class Index_Aboutserializer(serializers.ModelSerializer):
    class Meta:
        model = Index_About
        fields = "__all__"   
