from django.urls import path
# . --> Diretório que o arquivo está
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # http://127.0.0.1:8000/curso/1
    path('curso/<int:id>', views.curso, name='curso'),
    # http://127.0.0.1:8000/home/aula/1
    path('aula/<int:id>', views.aula, name = 'aula'),
]
