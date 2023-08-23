from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=100,
                                 required=True,
                                    widget=forms.TextInput(attrs={'placeholder': 'Username',
                                                                'class': 'form-control',
                                                                }))
    password = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Password',
                                                                    'class': 'form-control',
                                                                    }))
    
    class Meta:
        model = User
        fields = ['username', 'password']

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']
                
class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['title','description','status']
