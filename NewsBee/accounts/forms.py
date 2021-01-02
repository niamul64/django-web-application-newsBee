from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ExtentionUser


class UserReg(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2' )


class ExtentUser(forms.ModelForm):

    class Meta:
        model = ExtentionUser
        fields = ('fullName', 'country')