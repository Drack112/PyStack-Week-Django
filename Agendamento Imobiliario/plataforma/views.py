from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from .models import *

# Create your views here.
# bloquear a permissão de view, comente pode ver se estiver logado
@login_required(login_url="/auth/login")
def home(request):
    preco_minimo = request.GET.get("preco_minimo")
    preco_maximo = request.GET.get("preco_maximo")
    cidade = request.GET.get("cidade")
    tipo = request.GET.getlist("tipo")

    if preco_minimo or preco_maximo or cidade or tipo:

        if not preco_minimo:
            preco_minimo = 0
        if not preco_maximo:
            preco_maximo = 9999999999
        if not tipo:
            tipo = ["A", "C"]

        imoveis = (
            Imovei.objects.filter(valor__gte=preco_minimo)
            .filter(valor__lte=preco_maximo)
            .filter(tipo_imovel__in=tipo)
            .filter(cidade=cidade)
        )

    else:
        imoveis = Imovei.objects.all()

    imoveis = Imovei.objects.all()
    cidades = Cidade.objects.all()
    # {} tags para adicionar no html
    return render(request, "home.html", {"imoveis": imoveis, "cidades": cidades})


def imovel(request, id):
    imovel = get_object_or_404(Imovei, id=id)
    sugestoes = Imovei.objects.filter(cidade=imovel.cidade).exclude(id=id)[:2]
    return render(
        request, "imovel.html", {"imovel": imovel, "sugestoes": sugestoes, "id": id}
    )


def agendar_visitas(request):
    usuario = request.user
    dia = request.POST.get("dia")
    horario = request.POST.get("horario")
    id_imovel = request.POST.get("id_imovel")

    visitas = Visitas(imovel_id=id_imovel, usuario=usuario, dia=dia, horario=horario)

    visitas.save()

    return redirect("/agendamentos")


def agendamentos(request):
    visitas = Visitas.objects.filter(usuario=request.user)
    return render(request, "agendamentos.html", {"visitas": visitas})


def cancelar_agendamento(request, id):
    visitas = get_object_or_404(Visitas, id=id)
    visitas.status = "C"
    visitas.save()
    return redirect("/agendamentos")
