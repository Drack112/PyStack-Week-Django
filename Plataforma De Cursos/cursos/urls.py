from django.urls import path

# . --> Diretório que o arquivo está
from . import views

# URLS nao precisam de um template necessariamente, ambas podem apenas retornar uma pequena funçao
urlpatterns = [
    path("", views.home, name="home"),
    # http://127.0.0.1:8000/curso/1
    path("curso/<int:id>", views.curso, name="curso"),
    # http://127.0.0.1:8000/home/aula/1
    path("aula/<int:id>", views.aula, name="aula"),
    path("comentarios/", views.comentarios, name="comentarios"),
    path("processa_avaliacao/", views.processa_avaliacao, name="processa_avaliacao"),
]
