from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(APIUser, UserAdmin)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Order)