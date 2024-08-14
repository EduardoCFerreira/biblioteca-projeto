from django import forms
from bibliotech.models import Book
from collections import defaultdict
from django.core.exceptions import ValidationError

class LivroCriar(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)

        self._my_errors = defaultdict(list)

    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'cover',
            'quantidade',
            'category',
            'author',
            'emprestado'
        ]

    def clean(self, *args, **kwargs):
        super_clean = super().clean(*args, **kwargs)
        cleaned_data = self.cleaned_data

        title = cleaned_data.get('title')
        description = cleaned_data.get('description')

        # Caso queria fazer um erro aparecer em dois campos ao mesmo tempo,
        #  devemos usar isso:
        if title == description:
            self._my_erros['title'].append('O titulo nao pode ser igual a descrição')
            self._my_erros['description'].append('A descrição nao pode ser igual ao titulo')
            

        if self._my_errors:
            raise ValidationError(self._my_errors)

        return super_clean
    
    def clean_title(self):
        title = self.cleaned_data.get('title')

        if len(title) <= 0 :
            self._my_errors['title'].append('Titulo não pode ser vazio')

        return title