from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import APIUser

admin.site.register(APIUser, UserAdmin)