from django import forms
from django.contrib.auth.models import User


class UserLoginForm(forms.ModelForm):

    username = forms.CharField(label='username  ', widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput(), label='password  ')

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['username', 'password','first_name', 'last_name']


class UserUpdateForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), label='password  ')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password']

