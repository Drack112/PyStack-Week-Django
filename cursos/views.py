from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import Cursos, Aulas

# Create your views here.
def home(request):
    if request.session.get('usuario'):
        cursos = Cursos.objects.all()
        request_usuario = request.session.get('usuario')
        return render(request, 'home.html', {'cursos': cursos, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def curso(request, id):
    if request.session.get('usuario'):
        # Pegar o id do curso
        aulas = Aulas.objects.filter(curso = id)
        request_usuario = request.session.get('usuario')
        # Completar as variaveis vazias
        return render(request, 'curso.html', {'aulas': aulas, 'request_usuario': request_usuario})
    else:
        return redirect('/auth/login/?status=2')

def aula(request, id):
    if request.session.get('usuario'):
        aula = Aulas.objects.get(id = id)
        return render(request, 'aula.html', {'aula': aula})
    else:
        return redirect('/auth/login/?status=2')        