from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm,UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','degree']
    
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','degree']
