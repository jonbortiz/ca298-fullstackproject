from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from django.shortcuts import redirect
from .models import APIUser
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
        super(UserLoginForm, self).__inti__(*args, **kwargs)
    
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your Username'}))
    username = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your Password'}))
