import re

from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def add_attr(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

def add_placeholder(field, placeholder_val):
    add_attr(field, 'placeholder', placeholder_val)


#Essa funcao eh para que o usuario utilize todos os caracteres, sendo um maisculo, minusculo e numeros
def senha_forte(senha):
    regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9]).{8,}$')

    if not regex.match(senha):
        raise ValidationError((
            'Sua senha deve ter pelo menos 8 caracteres'
        ),
        code='invalid'
        )
    
class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['first_name'], 'Digite seu nome')
        add_placeholder(self.fields['last_name'], 'Digite seu sobrenome')
        add_placeholder(self.fields['username'], 'Digite seu username')
        add_placeholder(self.fields['email'], 'Digite seu email')

    email = forms.EmailField(
        error_messages={'required': 'Email e obrigatório'},
        label = 'E-mail',
        help_text='O email precisa ser valido',
    )

    password = forms.CharField(
        required=True,
        widget=forms.PasswordInput( attrs={
            'placeholder': 'Digite sua senha',
        }),
        validators= [senha_forte]
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput( attrs={
            'placeholder': 'Repita sua senha',
        })
    )

    """ Essa class Meta é utilizada pra colocar os campos que vamos querer no nosso formulario.
    Nesse caso, coloquei os campos: primeiro_nome, ultimo_nome, email e senha.
    """

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]


    def clean_email(self):
        email = self.cleaned_data.get('email', '')
        exists = User.objects.filter(email=email).exists()

        if exists:
            raise ValidationError(
                'User e-mail is already in use', code='invalid',
            )

        return email


    """Essa função é utlizada para ver se uma senha é igual a outra, caso as senhas forem diferentes como mostra a linha 70, ele levanta um erro no formulario"""
    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and Password2 must be equal',
                'password2': 'Password and Password2 must be equal'
            })