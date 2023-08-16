from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm ,UsernameField,PasswordChangeForm , PasswordResetForm , SetPasswordForm
from django.contrib.auth import password_validation



class Sign_up(UserCreationForm):
    password1 = forms.CharField(widget=forms.PasswordInput(),label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(),label = 'Confirm  Password')
    class Meta:
        model = User
        fields = ['username']
        # labels = {'first_name':'First Name','last_name':'Last Name','email':'Email'}
        widgets = {'username':forms.TextInput()}


class Log_in(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

