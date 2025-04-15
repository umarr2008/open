from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User


# forms for user signup and login views that create users and authenticate users in the database
class UserSignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number', 'username',  'password1', 'password2']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Familiyangizni kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'input100', 'placeholder': 'Emailingizni kiriting'}),
            'phone_number': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Telefon raqam'}),
            'username': forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username kiriting'}),
            'password1': forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Parolni kiriting'}),
            'password2': forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Parolni takrorlang'}),
        }


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input100', 'placeholder': 'Username kiriting'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input100', 'placeholder': 'Parolni kiriting'}))

