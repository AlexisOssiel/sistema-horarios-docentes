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
