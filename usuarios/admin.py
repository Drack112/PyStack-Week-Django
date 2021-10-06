from django.contrib import admin

# .models --> significa um módulo da pasta que estou
from .models import Usuario

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
  # Exibir certas cosias no painel de admin
  list_display = "nome", "email", "senha"

  # O que ele irá usar em pesquisa
  search_fields = "nome", "email"

  # Dados de leitura apenas
  readonly_fields = "senha",
