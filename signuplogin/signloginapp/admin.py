from django.contrib import admin

from .models import Userlogin


# admin.site.register(Userlogin)
@admin.register(Userlogin)
class UserLoginAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "gender", "username", "password")
