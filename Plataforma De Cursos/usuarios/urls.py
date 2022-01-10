from django.urls import path
# . --> Diretório que o arquivo está
from . import views

urlpatterns = [
    # http://127.0.0.1:8000/auth/cadastro/
    path("cadastro/", views.cadastro, name="cadastro"),
    # http://127.0.0.1:8000/auth/login/
    path("login/", views.login, name="login"),
    path("valida_cadastro/", views.valida_cadastro, name="valida_cadastro"),
    path("valida_login/", views.valida_login, name="valida_login"),
    path("sair/", views.sair, name="sair")    
]
