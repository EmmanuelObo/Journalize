from django.contrib.auth.models import User
from django.forms import ModelForm, forms
from django import forms


class UserLoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']

    username = forms.CharField(label="Username", widget=forms.TextInput(attrs={'placeholder': 'jbsmooth'}), required=True)
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'placeholder': 'shhhhh..'}))


class UserRegistrationForm(forms.Form):
    first_name = forms.CharField(label="First Name:", required=False)
    last_name = forms.CharField(label="Last Name:", required=False)
    username = forms.CharField(label="Username:", required=True)
    password = forms.CharField(widget=forms.PasswordInput())
    birth_date = forms.DateField(widget=forms.DateInput())
    profile_pic = forms.ImageField()