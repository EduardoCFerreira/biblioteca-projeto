from django import forms
from utils.django_forms import add_placeholder

class LoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['email'], 'Digite seu email')
        add_placeholder(self.fields['password'], 'Digite sua senha')

    email = forms.CharField()
    password = forms.CharField(
        widget= forms.PasswordInput()
    )