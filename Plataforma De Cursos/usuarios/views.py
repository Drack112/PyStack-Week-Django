from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario

import hashlib  # criar criptografia de senha


def cadastro(request):
    # Se o usuario estiver ja logado/cadastrado, direciona para a home
    if request.session.get("usuario") == True:
        return redirect('/home')
    # Status --> Filtrar status de registro
    status = request.GET.get("status")
    #                                        Criar variavel vazia
    return render(request, 'cadastro.html', {'status': status})


def login(request):
    # Se o usuario estiver ja logado/cadastrado, direciona para a home
    if request.session.get("usuario") == True:
        return redirect('/home')
    status = request.GET.get('status')
    return render(request, 'login.html', {'status': status})


def valida_cadastro(request):
    # Pegar os dados do FORMS
    nome = request.POST.get('nome')
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    usuario = Usuario.objects.filter(email=email)

    if len(usuario) > 0:
        return redirect('/auth/cadastro/?status=1')

    if len(nome.strip()) == 0 or len(email.strip()) == 0:
        return redirect('/auth/cadastro/?status=2')

    if len(senha) < 8 or len(senha) > 16:
        return redirect('/auth/cadastro/?status=3')

    try:
        # Senha com criptografia
        senha = hashlib.sha256(senha.encode()).hexdigest()
        # Definir os dados do usuario com que o user passou
        usuario = Usuario(nome=nome, email=email, senha=senha)
        # Salvar os dados no banco de dados
        usuario.save()

        return redirect('/auth/cadastro/?status=0')
    except:
        return redirect('/auth/cadastro/?status=4')


def valida_login(request):
    email = request.POST.get('email')
    senha = request.POST.get('senha')
    # Validar a senha de user
    senha = hashlib.sha256(senha.encode()).hexdigest()
    usuarios = Usuario.objects.filter(email=email).filter(senha=senha)

    if len(usuarios) == 0:
        return redirect('/auth/login/?status=1')
    elif len(usuarios) > 0:
        request.session['usuario'] = usuarios[0].id
        return redirect('/home/')


def sair(request):
    # Remover todas as sessions
    request.session.flush()
    return redirect("/auth/login")