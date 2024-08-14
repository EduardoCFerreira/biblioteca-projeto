from django import forms
from bibliotech.models import Book
from collections import defaultdict

class LivroCriar(forms.ModelForm):

    class Meta:
        model = Book
        fields = [
            'title',
            'description',
            'cover',
            'quantidade',
            'category',
            'author',
        ]