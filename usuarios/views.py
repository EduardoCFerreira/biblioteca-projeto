from django.urls import reverse
from django.http import Http404
from django.shortcuts import redirect, render
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'usuarios/pages/register_view.html',{
        'form': form,
        'form_action': reverse("usuarios:create"),
        })

def register_create(request):
    if not request.POST:
        raise Http404()
    
    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        data = form.save(commit=False)
        data.set_password(data.password)
        data.save()
        messages.success(request, 'Seu usuario foi criado, por favor faça login')

        del(request.session['register_form_data'])
        
    return redirect('usuarios:register')

def login_view(request):
    form = LoginForm()
    return render(request, 'usuarios/pages/login.html', {
        'form': form,
        'form_action': reverse('usuarios:login_create')
    })

def login_create(request):
    if not request.POST:
        raise Http404()
    
    form = LoginForm(request.POST)
    login_url = reverse('usuarios:login')

    if form.is_valid():
        authenticated_user = authenticate(
            username=form.cleaned_data.get('username', ''),
            password=form.cleaned_data.get('password', ''),
        )

        if authenticated_user is not None:
            messages.success(request, 'Você está logado')
            login(request, authenticated_user)
        else:
            messages.error(request, 'Nome ou senha errados')
    else:
        messages.error(request, 'Erro de validação')

    return redirect(login_url)