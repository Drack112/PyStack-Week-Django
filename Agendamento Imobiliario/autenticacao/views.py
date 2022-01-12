from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth


def cadastro(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "cadastro.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        senha = request.POST.get("senha")

        if (
            len(username.strip()) == 0
            or len(email.strip()) == 0
            or len(senha.strip()) == 0
        ):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return redirect("/auth/cadastro")

        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, "Usuário já existe")
            return redirect("/auth/cadastro")

        try:
            user = User.objects.create_user(
                username=username, email=email, password=senha
            )

            user.save()
            # Mensagens das TAGS em settings.py
            messages.add_message(
                request, constants.SUCCESS, "Usuário cadastrado com sucesso"
            )
            return redirect("/auth/login")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            return redirect("/auth/cadastro")

        # return HttpResponse(f"{username} {email} {senha}")


def login(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect("/")
        return render(request, "login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        senha = request.POST.get("senha")

        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, "Erro interno do sistema")
            return redirect("/auth/login")
        else:
            auth.login(request, usuario)
            return redirect("/")


def sair(request):
    auth.logout(request)
    return redirect("/auth/login")
