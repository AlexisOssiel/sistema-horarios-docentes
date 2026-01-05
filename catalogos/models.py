from django.db import models
from django.db import transaction

class Periodo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)  # ej. "2026-1"
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=False)

    class Meta:
        ordering = ["-fecha_inicio"]

    def __str__(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} ({estado})"

    def save(self, *args, **kwargs):
        with transaction.atomic():
            if self.activo:
                Periodo.objects.exclude(pk=self.pk).update(activo=False)
            super().save(*args, **kwargs)

class Docente(models.Model):
    nombre = models.CharField(max_length=80)
    apellido_paterno = models.CharField(max_length=80)
    apellido_materno = models.CharField(max_length=80, blank=True, default="")
    email = models.EmailField(blank=True, null=True, unique=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["apellido_paterno", "apellido_materno", "nombre"]

    def __str__(self):
        ap = self.apellido_paterno
        am = self.apellido_materno.strip()
        nom = self.nombre
        return f"{ap} {am} {nom}".replace("  ", " ").strip()

class Aula(models.Model):
    clave = models.CharField(max_length=30, unique=True)  # ej. "A-101"
    edificio = models.CharField(max_length=50, blank=True, default="")
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["clave"]

    def __str__(self):
        return self.clave
