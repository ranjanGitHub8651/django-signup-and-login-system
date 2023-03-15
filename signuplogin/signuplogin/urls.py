from django.contrib import admin
from django.urls import path

from signloginapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signUp),
    path('login/', views.LoginPage),
    path('user_detail/<int:id>/', views.afterLoginPage),
]
