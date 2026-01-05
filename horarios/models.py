from django.db import models
from django.core.exceptions import ValidationError
from catalogos.models import Docente, Aula, MateriaGrupo, Periodo


class Horario(models.Model):
    DIAS_SEMANA = (
        (1, "Lunes"),
        (2, "Martes"),
        (3, "Miércoles"),
        (4, "Jueves"),
        (5, "Viernes"),
        (6, "Sábado"),
    )

    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    materia_grupo = models.ForeignKey(MateriaGrupo, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)

    dia_semana = models.PositiveSmallIntegerField(choices=DIAS_SEMANA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["dia_semana", "hora_inicio"]

    def __str__(self):
        return f"{self.materia_grupo} | {self.get_dia_semana_display()} {self.hora_inicio}-{self.hora_fin}"


    def clean(self):
        if self.hora_inicio >= self.hora_fin:
            raise ValidationError("La hora de inicio debe ser menor a la hora de fin.")

        qs = Horario.objects.filter(
            periodo=self.periodo,
            dia_semana=self.dia_semana,
            activo=True
        ).exclude(pk=self.pk)

        # Traslape por DOCENTE
        if qs.filter(
            docente=self.docente,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exists():
            raise ValidationError(
                "Conflicto: el docente ya tiene una clase asignada en este horario."
            )

        # Traslape por AULA
        if qs.filter(
            aula=self.aula,
            hora_inicio__lt=self.hora_fin,
            hora_fin__gt=self.hora_inicio
        ).exists():
            raise ValidationError(
                "Conflicto: el aula ya está ocupada en este horario."
            )
