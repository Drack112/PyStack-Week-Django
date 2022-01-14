from django.urls import path

from .views import home, imovel, agendar_visitas, agendamentos, cancelar_agendamento

urlpatterns = [
    path("", home, name="home"),
    path("imovel/<str:id>", imovel, name="imovel"),
    path("agendar_visitar", agendar_visitas, name="agendar_visitas"),
    path("agendamentos", agendamentos, name="agendamentos"),
    path(
        "cancelar_agendamento/<str:id>",
        cancelar_agendamento,
        name="cancelar_agendamento",
    ),
]
