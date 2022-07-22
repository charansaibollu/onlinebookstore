"""charan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from bookapp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view()),
    path('aboutus/', Aboutus, name='aboutus'),
    path('contactus/', Contactus, name='contactus'),
    path('login/', loginPage, name='login'),
    path('addbook/',InsertInput,name='addbook'),
    path('addbook/insert/',Inser,name='insert'),
    path('display/',DisplayView.as_view()),
    path('deleteinput/',DeleteInput,name='deleteinput'),
    path('deleteinput/delete/',Delete,name='delete'),
    path('updateinput/',UpdateInput,name='updateinput'),
    path('updateinput/update/',Update,name='update'),
    path('register/', registerPage, name='register'),
    path('logout/', logoutPage, name='logout'),
    path('adminpage/',AdminpageView.as_view(),name='adminpage'),
    path('customerpage/',Customerpage,name='customerpage'),
    path('logout/',logoutPage,name='logout'),
    path('addtocart/<str:pk>/', addtocart, name='addtocart'),
    path('viewcart/', viewcart,name='viewcart'),
    path('deletecart/',deletecart,name='deletecart'),
    path('removecart/<str:pk>/',removecart,name='removecart'),
]
