from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from usuarios.form import RegisterForm


def cadastro_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'usuarios/pages/cadastro-view.html', {
        'form': form,
        'form_action': reverse('usuarios:create'),
    })


def cadastro_create(request):
    if not request.POST:
        raise Http404()
    
    POST= request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(user.password)
        user.save()
        messages.success(request, 'Seu usuario foi criado')

        #del = deleta alguma chave de dicionario
        del(request.session['register_form_data'])
        
    return redirect('usuarios:cadastro')


def login_view(request):
    return render(request, 'usuarios/pages/login-view.html')

def login_create(request):
    ...