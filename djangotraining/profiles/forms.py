from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.db import models
from django.contrib.auth.models import User
from .models import BasicProfile


class EditUserForm(UserChangeForm):
	password = forms.CharField(label="",  widget=forms.TextInput(attrs={'type':'hidden'}))
	first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dein Vorname'}))
	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password',)

class BasicProfileForm(forms.ModelForm):
	class Meta:
		model = BasicProfile
		fields = ('user', 'street', 'city_name', 'city_code', 'tel_private')