from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .models import Userlogin


def signUp(request):
    error = 'Password and repeat password dose not matched.'
    if request.method=="POST":
        add = Userlogin()
        add.name = request.POST.get('name')
        add.email = request.POST.get('email')
        add.username = request.POST.get('username')
        first_pass = request.POST.get('password')
        re_pass = request.POST.get('rpassword')
        if(first_pass == re_pass):
            add.password = first_pass
        else:
            return render(request, 'signloginapp/signup.html', {'message': error})
        add.save()
        return render(request, 'signloginapp/login.html')
    return render(request, 'signloginapp/signup.html')



def LoginPage(request, user, password):
    error_login = 'Password or username does not matched.'
    login = Userlogin.objects.filter(username=user, password=password)
    print(login, "\n\n\n\n")
    if login:
        return redirect('user_detail/')

    return render(request, 'signloginapp/login.html', {'message': error_login})

@login_required
def afterLoginPage(request, id):
    user_date = Userlogin.objects.get(id=id)
    return render(request, 'signloginapp/user_details.html', {'user': user_date})