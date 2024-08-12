from django.contrib import admin
from bibliotech.models import Author, Category, Book, Emprestimo

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    ...

class CategoryAdmin(admin.ModelAdmin):
    ...

class BookAdmin(admin.ModelAdmin):
    ...

class EmprestimoAdmin(admin.ModelAdmin):
    ...

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    ...

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'emprestado', 'author',]
    list_display_links = 'title', 'author',
    search_fields = 'id', 'title', 'description', 'slug',
    list_filter = 'category', 'author', 'emprestado',
    list_per_page = 10

@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    ...