from django import forms
from django.contrib.auth.forms import UserCreationForm
from.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=120,widget=forms.PasswordInput )





class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')