from django.contrib import admin
from django.urls import path, include

from app1 import views

urlpatterns = [
    path('home/' , views.home ,name='home') ,
    path('about' , views.about , name='about') ,
    path('contact' , views.contact , name='contact') ,
    path('gallery' , views.gallery ,name='gallery') ,
    path('note' , views.note , name='note'),
    path('' ,views.signup , name='signup'),
    path('signin' ,views.signin , name='signin'),
    path('show' ,views.show , name='show')
]