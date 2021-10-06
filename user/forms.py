from django import forms
from user.models import User
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('student_number','email','first_name', 'last_name','level_and_section',)

class UserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('student_number','email','first_name', 'last_name','level_and_section')

class LoginForm(AuthenticationForm):
    email = forms.CharField(required=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address', 'autofocus':'autofocus', 'required':'required'}))
    password = forms.CharField(required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'********','autocomplete': 'off','data-toggle': 'password', 'required': 'required'}))
