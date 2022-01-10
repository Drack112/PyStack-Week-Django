from django.contrib import admin
from .models import Cursos, Aulas, Comentarios, NotasAulas

# Register your models here.

admin.site.register(Cursos)
admin.site.register(Aulas)


@admin.register(Comentarios)
class ComentariosAdmin(admin.ModelAdmin):
    list_display = "usuario", "comentario", "data", "aula"
    search_fields = "usuario", "comentario"


@admin.register(NotasAulas)
class NotasAdmin(admin.ModelAdmin):
    list_display = "aula", "nota", "usuario"
    search_fields = "usuario", "aula"
