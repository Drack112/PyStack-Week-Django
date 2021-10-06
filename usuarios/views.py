from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Usuario

import hashlib # criar criptografia de senha

def cadastro(request):
  # Status --> Filtrar status de registro
  status = request.GET.get("status")
  #                                        Criar variavel vazia
  return render(request, 'cadastro.html', {'status': status})

def login(request):
  # Retornar o html de templates
  return render(request, 'login.html')

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
