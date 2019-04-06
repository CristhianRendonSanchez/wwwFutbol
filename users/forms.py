from django import forms
from apuestas.models import UserProfile


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = "__all__"


class UserPayoffForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['dni', 'name', 'lastname', 'email', 'balance']
