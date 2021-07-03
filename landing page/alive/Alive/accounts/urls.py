from django.contrib import admin
from django.urls import path, include
from accounts import views

urlpatterns = [

    path('home' , views.home , name="home") ,
    path('' , views.login_attempt , name='login'),
    path('otp' , views.otp , name='otp'),
    path('register' , views.register , name='register'),
    path('login-otp', views.login_otp , name='login_otp'),
    
        
]