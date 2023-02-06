import os

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.contrib.messages import constants
from django.conf import settings

from hashlib import sha256

from .utils import password_confirm
from .email import send_email
from .models import Ativacao


# Create your views here.
def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(request, "/")
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("usuario")
        senha = request.POST.get("senha")
        email = request.POST.get("email")
        confirmar_senha = request.POST.get("confirmar_senha")

        if not password_confirm.password_is_valid(request, senha, confirmar_senha):
            return redirect("/auth/cadastro")

        try:
            user = User.objects.create_user(
                username=username, email=email, password=senha, is_active=False
            )

            user.save()

            token = sha256(f"{username}{email}".encode()).hexdigest()
            ativacao = Ativacao(token=token, user=user)
            ativacao.save()

            path_template = os.path.join(
                settings.BASE_DIR,
                "autenticacao/templates/emails/cadastro_confirmado.html",
            )
            send_email.email_html(
                path_template,
                "Cadastro Confirmado",
                [
                    email,
                ],
                username=username,
                link_ativacao=f"127.0.0.1:8000/auth/ativar_conta/{token}",
            )

            messages.add_message(
                request, constants.SUCCESS, "Cadastro realizado com sucesso"
            )

            return redirect("/auth/logar")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno no sistema")
            return redirect("/auth/cadastro")

    # vQM5KaFtj4R8REN


def logar(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect(request, "/")
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("usuario")
        senha = request.POST.get("senha")

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(
                request, constants.ERROR, "Username ou senha inválidos"
            )
            return redirect("/auth/logar")
        else:
            auth.login(request, usuario)
            return redirect("/")


def sair(request):
    auth.login(request)
    return redirect(request, "/auth/logar")


def ativar_conta(request, token):
    token = get_object_or_404(Ativacao, token=token)

    if token.ativo:
        messages.add_message(request, constants.WARNING, "Esse token já foi usado")
        return redirect("/auth/logar")

    user = User.objects.get(username=token.user.username)
    user.is_active = True
    user.save()

    token.ativo = True
    token.save()

    messages.add_message(request, constants.SUCCESS, "Conta ativada com sucesso")
    return redirect("/auth/logar")
