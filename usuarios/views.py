from django.urls import reverse
from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
        return redirect(reverse('usuarios:login'))
        
    return redirect('usuarios:cadastro')


def login_view(request):
    form = LoginForm()
    return render(request, 'usuarios/pages/login-view.html', {
        'form': form,
        'form_action': reverse('usuarios:login')
    })

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)
    login_url = reverse('usuarios:login')

    if form.is_valid():
        authenticated_user = authenticate(
            email=form.cleaned_data.get('email', ''),
            password=form.cleaned_data.get('password', '')          
        )
        if authenticated_user is not None:
            messages.success(request, 'Voce esta logado')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Algo esta errado')
    else:
        messages.error(request, 'Email ou Senha errados')

    return redirect(login_url)

@login_required(login_url='usuarios:login', redirect_field_name='next')
def logout_view(request):
    if not request.POST:
        return redirect(reverse('usuarios:login'))
    
    if request.POST.get('email') != request.user.email:
        return redirect(reverse('usuarios:login'))

    logout(request)
    return redirect(reverse('usuarios:login'))

@login_required(login_url='usuarios:login', redirect_field_name='next')
def emprestimos(request):
    return render(request, 'usuarios/pages/emprestimos.html')