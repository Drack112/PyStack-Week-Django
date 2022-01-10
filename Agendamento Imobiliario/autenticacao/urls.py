from django.urls import path
from .views import cadastro, login

urlpatterns = [
    path("cadastro/", cadastro, name="cadastro"),
    path("login/", login, name="login")
]
