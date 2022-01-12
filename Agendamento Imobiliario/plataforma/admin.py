from django.contrib import admin
from .models import *


@admin.register(Imovei)
class ImoveiAdmin(admin.ModelAdmin):
    list_display = ("rua", "valor", "quartos", "tamanho", "cidade", "tipo")
    # Valores para editar na aba principal
    list_editable = ("valor", "tipo")
    # Filtros
    list_filter = ("cidade", "tipo")


admin.site.register(DiasVisita)
admin.site.register(Horario)
admin.site.register(Imagem)
admin.site.register(Cidade)
admin.site.register(Visitas)
