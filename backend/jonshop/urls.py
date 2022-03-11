from django.contrib import admin
from django.urls import path, include
from . import views
from jonshop.forms import *
from rest_framework import routers

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'basket', views.BasketViewSet)
router.register(r'orders', views.OrderViewSet)
router.register(r'users', views.APIUserViewSet)


urlpatterns = [
    path('', views.index, name='homepage'),
    path('products/<int:prodid>', views.product_individual, name="individual product"),
    path('addbasket/<int:prodid>', views.add_to_basket, name="add_basket"),
    path('basket/', views.show_basket, name="show_basket"),
    path('removebasket/<int:sbi>', views.remove_basket, name="remove_basket"),
    path('order/', views.order, name='order'),
    path('orderhistory/', views.previous_orders, name="order_history"),
    path('login/', views.LoginView.as_view(template_name="login.html", authentication_form=UserLoginForm)),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.UserSignupView.as_view(), name="register"),
    path('apiregister/', views.UserRegistrationAPIView.as_view(), name="api_register"),
    path('apiadd/', views.AddBasketItemAPIView.as_view(), name="api_add_to_basket"),
    path('apiremove/', views.RemoveBasketItemAPIView.as_view(), name="api_remove_from_basket"),
    path('apicheckout/', views.CheckoutAPIView.as_view(), name="api_checkout"),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include(router.urls))
]
