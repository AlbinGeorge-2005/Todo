from django import forms
from django.contrib.auth.models import User
from Todoapp.models import Todo
from django.contrib.auth.forms import UserCreationForm


class TodoForm(forms.ModelForm): # 

    class Meta:

        model=Todo

        fields=["title","description","status"]
      
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'description':forms.Textarea(attrs={'class':'form-control mb-3'}),
            'status': forms.Select(attrs={'class':'form-select mb-3'}),
        }


class ResgistrationForm(UserCreationForm): # Sign Up Page
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    class Meta:
        model=User
        fields=['username','email','password1','password2']
        widgets={

            'username':forms.TextInput(attrs={'class':'form-control mb-3'}),
            'email':forms.TextInput(attrs={'class':'form-control mb-3'})
        }


class LoginForm(forms.Form):# Log in Page
    
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control mb-3'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control mb-3'}))
    






