from django.urls import path

from .views import home, imovel

urlpatterns = [
    path("", home, name="home"),
    path("imovel/<str:id>", imovel, name="imovel"),
]
