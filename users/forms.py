from django import forms
from apuestas.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['password', 'is_superuser', 'email', 'name', 'lastname', 'balance', 'dni', 'is_active']


class UserPayoffForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dni', 'name', 'lastname', 'email', 'balance']


class LoginForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['email', 'password']