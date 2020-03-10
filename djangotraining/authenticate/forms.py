from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    username = forms.CharField(label="", help_text="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dein Benutzername'}))
    #email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Deine Email-Adresse'}))
    #first_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dein Vorname'}))
    #last_name = forms.CharField(max_length=100, label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dein Nachname'}))
    password1 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dein Passwort'}))
    password2 = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Wiederhole dein Passwort'}))
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )  # 'first_name', 'last_name', 'email',

    def __init__(self, *args, **kwargs):
	    super(SignUpForm, self).__init__(*args, **kwargs)
