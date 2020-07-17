"""EShop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
import Store.views as views
from Store.middlewares.auth import auth_middleware
from Store.middlewares.cart_present import cart_present_middleware

urlpatterns = [
    path('', views.Index.as_view(), name='homepage'),
    path('<str:name>/',
         views.Index.as_view(), name="homepageloggedin"),
    path('signup', views.Signupform.as_view()),
    path('login', views.Loginform.as_view(), name="login"),
    path('logout', views.logout, name='logout'),
    path('cart', cart_present_middleware(views.Cart.as_view()), name='cart'),
    path('check-out', auth_middleware(views.Check_out.as_view()), name='checkout'),
    path('orders', auth_middleware(views.Orders.as_view()), name="orders"),
]
