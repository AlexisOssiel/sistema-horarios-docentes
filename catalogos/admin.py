from django.contrib import admin
from .models import Periodo

@admin.register(Periodo)
class PeriodoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "fecha_inicio", "fecha_fin", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre",)

from .models import Docente

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ("apellido_paterno", "apellido_materno", "nombre", "email", "activo")
    list_filter = ("activo",)
    search_fields = ("nombre", "apellido_paterno", "apellido_materno", "email")

from .models import Aula

@admin.register(Aula)
class AulaAdmin(admin.ModelAdmin):
    list_display = ("clave", "edificio", "capacidad", "activo")
    list_filter = ("activo",)
    search_fields = ("clave", "edificio")

from .models import MateriaGrupo

@admin.register(MateriaGrupo)
class MateriaGrupoAdmin(admin.ModelAdmin):
    list_display = ("nombre_materia", "grado", "grupo", "clave", "activo")
    list_filter = ("grado", "grupo", "activo")
    search_fields = ("nombre_materia", "clave")
