from django import forms
from basic_app.models import UserProfileInfo
from django.contrib.auth.models import User

# Preparning Model Form


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    # portfolio = forms.URLField(required=False)
    # picture = forms.ImageField(required=False)

    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
