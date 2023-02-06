from django.urls import path

from autenticacao.views import logar, cadastro, sair, ativar_conta

urlpatterns = [
    path("cadastro", cadastro, name="cadastro"),
    path("logar", logar, name="logar"),
    path("sair", sair, name="logout"),
    path("ativar_conta/<str:token>", ativar_conta, name="ativar_conta"),
]
