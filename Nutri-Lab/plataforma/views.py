from datetime import datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.messages import constants
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404

from .models import Pacientes, DadosPaciente, Refeicao, Opcao


@login_required(login_url="/auth/logar/")
def pacientes(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, "pacientes.html", {"pacientes": pacientes})
    elif request.method == "POST":
        nome = request.POST.get("nome")
        sexo = request.POST.get("sexo")
        idade = request.POST.get("idade")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")

        if (
            (len(nome.strip()) == 0)
            or (len(sexo.strip()) == 0)
            or (len(idade.strip()) == 0)
            or (len(email.strip()) == 0)
            or (len(telefone.strip()) == 0)
        ):
            messages.add_message(request, constants.ERROR, "Preencha todos os campos")
            return redirect("/pacientes/")

        if not idade.isnumeric():
            messages.add_message(request, constants.ERROR, "Digite uma idade válida")
            return redirect("/pacientes/")

        paciente = Pacientes.objects.filter(email=email)

        if paciente.exists():
            messages.add_message(
                request, constants.ERROR, "Já existe um paciente com esse E-mail"
            )
            return redirect("/pacientes/")

        try:
            p1 = Pacientes(
                nome=nome,
                sexo=sexo,
                idade=idade,
                telefone=telefone,
                nutri=request.user,
            )

            p1.save()
            messages.add_message(
                request, constants.SUCCESS, "Paciente cadastrado com sucesso!"
            )
            return redirect("/pacientes/")
        except:
            messages.add_message(request, constants.ERROR, "Erro interno no sistema")
            return redirect("/pacientes")


@login_required(login_url="/auth/logar/")
def dados_paciente_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, "dados_paciente_listar.html", {"pacientes": pacientes})


@login_required(login_url="/auth/logar/")
def dados_paciente(request, id):  # id que veio pela url
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/dados_paciente/")

    if request.method == "GET":
        dados_paciente = DadosPaciente.objects.filter(paciente=paciente)
        return render(
            request,
            "dados_paciente.html",
            {"paciente": paciente, "dados_paciente": dados_paciente},
        )
    elif request.method == "POST":
        peso = request.POST.get("peso")
        altura = request.POST.get("altura")
        gordura = request.POST.get("gordura")
        musculo = request.POST.get("musculo")

        hdl = request.POST.get("hdl")
        ldl = request.POST.get("ldl")
        colesterol_total = request.POST.get("ctotal")
        triglicerídios = request.POST.get("triglicerídios")

        paciente = DadosPaciente(
            paciente=paciente,
            data=datetime.now(),
            peso=peso,
            altura=altura,
            percentual_gordura=gordura,
            percentual_musculo=musculo,
            colesterol_hdl=hdl,
            colesterol_ldl=ldl,
            colesterol_total=colesterol_total,
            trigliceridios=triglicerídios,
        )

        paciente.save()

        messages.add_message(request, constants.SUCCESS, "Dados cadastrado com sucesso")

        return redirect("/dados_paciente/")


from django.views.decorators.csrf import csrf_exempt


@login_required(login_url="/auth/logar/")
@csrf_exempt
def grafico_peso(request, id):
    paciente = Pacientes.objects.get(id=id)
    dados = DadosPaciente.objects.filter(paciente=paciente).order_by("data")

    pesos = [dado.peso for dado in dados]
    labels = list(range(len(pesos)))
    data = {"peso": pesos, "labels": labels}
    return JsonResponse(data)


def plano_alimentar_listar(request):
    if request.method == "GET":
        pacientes = Pacientes.objects.filter(nutri=request.user)
        return render(request, "plano_alimentar_listar.html", {"pacientes": pacientes})


def plano_alimentar(request, id):
    paciente = get_object_or_404(Pacientes, id=id)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/plano_alimentar_listar/")

    if request.method == "GET":
        r1 = Refeicao.objects.filter(paciente=paciente).order_by("horario")
        opcao = Opcao.objects.all()
        return render(
            request,
            "plano_alimentar.html",
            {"paciente": paciente, "refeicao": r1, "opcao": opcao},
        )


def refeicao(request, id_paciente):
    paciente = get_object_or_404(Pacientes, id=id_paciente)
    if not paciente.nutri == request.user:
        messages.add_message(request, constants.ERROR, "Esse paciente não é seu")
        return redirect("/dados_paciente/")

    if request.method == "POST":
        titulo = request.POST.get("titulo")
        horario = request.POST.get("horario")
        carboidratos = request.POST.get("carboidratos")
        proteinas = request.POST.get("proteinas")
        gorduras = request.POST.get("gorduras")

        r1 = Refeicao(
            paciente=paciente,
            titulo=titulo,
            horario=horario,
            carboidratos=carboidratos,
            proteinas=proteinas,
            gorduras=gorduras,
        )

        r1.save()

        messages.add_message(request, constants.SUCCESS, "Refeição cadastrada")
        return redirect(f"/plano_alimentar/{id_paciente}")


def opcao(request, id_paciente):
    if request.method == "POST":
        id_refeicao = request.POST.get("refeicao")
        imagem = request.FILES.get("imagem")
        descricao = request.POST.get("descricao")

        o1 = Opcao(
            refeicao_id=id_refeicao,
            imagem=imagem,
            descricao=descricao,
        )

        o1.save()

        messages.add_message(request, constants.SUCCESS, "Opção cadastrada")
        return redirect(f"/plano_alimentar/{id_paciente}")
