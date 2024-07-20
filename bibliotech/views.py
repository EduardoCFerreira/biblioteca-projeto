from django.http import Http404, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404

from bibliotech.models import Book, Emprestimo
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    livros = Book.objects.all().order_by('-id')
    return render (request, 'bibliotech/pages/home.html', context={
        'livros': livros,
    })

def emprestimo(request):
    usuario = User.objects.filter(is_staff=True)
    emprestimo = Emprestimo.objects.filter()
    livros = Book.objects.all().order_by('-id')
    return render (request, 'bibliotech/pages/emprestimo.html', context={
        'livros': livros,
    })

"""
if usuario is True:
    return render(request, bibliotech/pages/emprestimo.html)
"""

def category(request, category_id):
    livros = get_list_or_404(
        Book.objects.filter(
            category__id=category_id
        ).order_by('-id')
    )

    return render(request, 'bibliotech/pages/category.html', context={
        'livros': livros,
        'title': f'{livros[0].category.name}'
    })

def book(request, id):
    livro = get_object_or_404(Book, id)

    return render(request, 'bibliotech/pages/livro.html', context={
        'livro': livro,
        'is_detail_page': True
    })

def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404
    
    livros = Book.objects.filter(
        title__icontains=search_term
    ).order_by('-id')

    return render(request, 'bibliotech/pages/search.html', context={
        'page_title': f'Search for {search_term} |',
        'books': livros,
    })