from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from .models import Image

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']


    def clean_confirm_password(self):
        cd = self.cleaned_data
        if cd['confirm_password'] != cd['password']:
            raise forms.ValidationError("Password don't match")
        return cd['confirm_password']


class LoginForm(AuthenticationForm):
    username = UsernameField(
        widget=forms.TextInput(attrs={'class': 'input', 'autofocus': True, 'placeholder': 'username'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'password'}))


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['name', 'cover']
