from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from App_Login.models import UserProfileModel


class CreateNewUserForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={'placeholder': 'Create Username'}))
    email = forms.EmailField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password1 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Create Password'}))
    password2 = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Create Password'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class EditUserProfileForm(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = UserProfileModel()
        exclude = ['user', ]
