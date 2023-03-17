from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib.auth import logout

from .models import Userlogin


def signUp(request):
    error = "Password and repeat password dose not matched."
    if request.method == "POST":
        add = Userlogin()
        add.name = request.POST.get("name")
        add.email = request.POST.get("email")
        add.gender = request.POST.get("gender")
        add.username = request.POST.get("username")
        first_pass = request.POST.get("password")
        re_pass = request.POST.get("rpassword")
        if first_pass == re_pass:
            add.password = first_pass
        else:
            return render(request, "signloginapp/signup.html", {"message": error})
        add.save()
        return render(request, "signloginapp/login.html")
    return render(request, "signloginapp/signup.html")


def redirectLoginPage(request):
    return render(request, "signloginapp/login.html")


def LoginPage(request):
    print(request, "request")
    error_login = "Password or username does not matched."
    if request.method == "POST":
        print("LOGIN PAGE 1 IF BLOCK \n\n\n\n")
        username = request.POST["username"]
        password = request.POST["password"]
        login = Userlogin.objects.filter(username=username, password=password)
        print(login, "LOGIN PAGE 1 IF BLOCK \n\n\n\n")

        print(login, "\n\n\n\n\n")
        if login:
            # return render(request, "signloginapp/user_details.html")
            return redirect("../user_detail/")

    return render(request, "signloginapp/login.html", {"message": error_login})


def afterLoginPage(request, id):
    user_date = Userlogin.objects.get(id=id)
    print(user_date, "USER DATE \n\n\n\n")
    return render(request, "signloginapp/user_details.html", {"user": user_date})


def LogoutUser(request):
    logout(request)
    return redirect("../loginpage/")
