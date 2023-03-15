from django import forms

from .models import Userlogin


class UserForm(forms.ModelForm):
    class Meta:
        model = Userlogin
        widgets = {
            # 'email': forms.EmailInput(),
            'password': forms.PasswordInput(),
        }