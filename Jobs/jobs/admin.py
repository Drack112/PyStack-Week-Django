from django.contrib import admin

# Register your models here.
from jobs.models import Jobs, Referencias


@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    list_display = (
        "titulo",
        "categoria",
        "prazo_entrega",
        "preco",
        "profissional",
        "reservado",
        "status",
    )
    list_filter = ("profissional", "categoria")
    search_fields = ("titulo",)


admin.site.register(Referencias)
