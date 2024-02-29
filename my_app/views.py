from django.shortcuts import render,redirect
from rest_framework.permissions import AllowAny
from rest_framework.generics import (ListAPIView, RetrieveAPIView,
                                     ListCreateAPIView, CreateAPIView,
                                     UpdateAPIView,DestroyAPIView)
from my_app.models import *
from my_app.serializers import *
from my_app.filter import ModelFilter,ProductFilter
from django_filters.rest_framework.backends import DjangoFilterBackend

class IndexListAPIView(ListAPIView):
    queryset = Index.objects.all()
    serializer_class = IndexSerializer
    
    
class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ProductFilter

class ProductCreateAPIView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDestroyAPIView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class BlogListAPIView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSeializer


class BlogRetrieveAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSeializer
    lookup_field = 'id'

class ContactCreateAPIView(CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = BlogSeializer

class SosialMediaListAPIView(ListAPIView):
    queryset = SosialMedia.objects.all()
    serializer_class = SosialMediaserializer


class MainDetailsListAPIView(ListAPIView):
    queryset = MainDetails.objects.all()
    serializer_class = MainDetailsserializer

class AskListAPIView(ListAPIView):
    queryset = Ask.objects.all()
    serializer_class = Askserializer

class ModelListAPIView(ListAPIView):
    queryset = Model.objects.all()
    serializer_class = Modelserializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = ModelFilter

class MarkaListAPIView(ListAPIView):
    queryset = Marka.objects.all()
    serializer_class = Markaseializer

class Index_AboutListAPI(ListAPIView):
    queryset = Index_About.objects.all()
    serializer_class = Index_Aboutserializer




