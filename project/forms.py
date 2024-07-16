from django import forms
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"id":"required"}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"id":"required"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"id":"required"}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]