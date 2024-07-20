from django.shortcuts import render
from django.http import Http404
from django.shortcuts import redirect, render
from django.contrib import messages
from usuarios.form import RegisterForm


def cadastro_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'usuarios/pages/cadastro-view.html', {
        'form': form,
    })


def cadastro_create(request):
    if not request.POST:
        raise Http404()
    
    POST= request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(POST)

    if form.is_valid():
        form.save()
        messages.success(request, 'Seu usuario foi criado')

        #del = deleta alguma chave de dicionario
        del(request.session['register_form_data'])
        
    return redirect('usuarios:cadastro')
