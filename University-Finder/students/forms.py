from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    username = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(widget=forms.PasswordInput)
    first_name = forms.CharField()
    last_name = forms.CharField()

    username.widget.attrs.update({'placeholder': "Username"})
    password1.widget.attrs.update({'placeholder': 'New Password'})
    password2.widget.attrs.update({'placeholder': 'Re-enter Password'})
    first_name.widget.attrs.update({'placeholder': 'First Name'})
    last_name.widget.attrs.update({'placeholder': 'Surname'})

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


class DetailsForm(ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name',
                  'student_id', 'email', 'level', 'degree_name']


NUMS = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Others', 'Others'),
]

class CHOICES(forms.Form):
    NUMS = forms.CharField(widget=forms.RadioSelect(choices=NUMS))

