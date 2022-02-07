from django.contrib import admin
from django.urls import path, include
from . import views
from jonshop.forms import *

urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/<int:prodid>', views.product_individual, name="individual product"),
    path('addbasket/<int:prodid>', views.add_to_basket, name="add_basket"),
    path('basket/', views.show_basket, name="show_basket"),
    path('removebasket/<int:sbi>', views.remove_basket, name="remove_basket"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.UserSignupView.as_view(), name="register")
]
