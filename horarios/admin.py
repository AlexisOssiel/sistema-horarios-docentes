from django.contrib import admin
from .models import Horario


@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = (
        "materia_grupo",
        "docente",
        "aula",
        "get_dia",
        "hora_inicio",
        "hora_fin",
        "periodo",
        "activo",
    )
    list_filter = ("periodo", "dia_semana", "docente", "aula")
    search_fields = ("materia_grupo__nombre_materia", "docente__nombre")

    def get_dia(self, obj):
        return obj.get_dia_semana_display()

    get_dia.short_description = "Día"
