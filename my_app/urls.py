from django.urls import path
from my_app.views import *

urlpatterns = [
    path("index/list",IndexListAPIView.as_view(), name='index-list'),
    path("product/list", ProductListAPIView.as_view(), name='product-list'),
    path("product/create", ProductCreateAPIView.as_view(), name='product-create'),
    path("product/detail/<id>/", ProductRetrieveAPIView.as_view(), name='product-detail'),
    path("product/destry",ProductDestroyAPIView.as_view(), name='product-destroy'),
    path("product/destry",ProductDestroyAPIView.as_view(), name='product-destroy'),
    path("contact/create",ContactCreateAPIView.as_view(), name='contact-create'),
    path("blog/list",BlogListAPIView.as_view(), name='blog-list'),
    path("blog/retrieve/<id>/'",BlogRetrieveAPIView.as_view(), name='blog-retrieve'),
    path("sosial/media",SosialMediaListAPIView.as_view(), name='sosial-media'),
    path("main/detail",MainDetailsListAPIView.as_view(), name='main-detail'),
    path("ask/list", AskListAPIView.as_view(), name='ask-list'),
    path("model/list", ModelListAPIView.as_view(), name='model-list'),
    path("marka/list", MarkaListAPIView.as_view(), name='marka-list'),
    path("index_about/list", Index_AboutListAPI.as_view(), name='index_about-list'),
    

]