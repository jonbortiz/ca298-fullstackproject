from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import redirect
from .models import *
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = APIUser
    
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.save()
        return user

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username'}))
    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Password'}))

class OrderForm(ModelForm):
    shipping_addr = forms.CharField(label="Shipping Address",widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Shipping address', 'id': 'ship-addr'}))
    class Meta:
        model = Order
        fields = ['shipping_addr']