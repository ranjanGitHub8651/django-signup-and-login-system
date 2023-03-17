from django.contrib import admin
from django.urls import path

from signloginapp import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.signUp),
    path("login/", views.LoginPage),
    path("loginpage/", views.redirectLoginPage),
    path("user_detail/<int:id>/", views.afterLoginPage),
    path('logout/', views.LogoutUser),
]
