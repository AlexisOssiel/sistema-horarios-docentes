from django.shortcuts import render
from .models import Horario

def horarios_por_docente(request, docente_id):
    horarios = Horario.objects.filter(docente_id=docente_id, activo=True)
    return render(request, "horarios/horarios_por_docente.html", {"horarios": horarios})

def horarios_por_grupo(request, grupo_id):
    horarios = Horario.objects.filter(materia_grupo_id=grupo_id, activo=True)
    return render(request, "horarios/horarios_por_grupo.html", {"horarios": horarios})

from django.http import HttpResponse
from .models import Horario
import csv

def reporte_por_docente(request, docente_id):
    horarios = Horario.objects.filter(docente_id=docente_id, activo=True)
    
    # Crear la respuesta HTTP con el formato CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_docente.csv"'
    
    # Crear el objeto writer de CSV
    writer = csv.writer(response)
    
    # Escribir los encabezados
    writer.writerow(['Materia', 'Aula', 'Hora', 'Día'])
    
    # Escribir los datos de cada horario
    for horario in horarios:
        writer.writerow([horario.materia_grupo.nombre_materia, 
                         horario.aula.clave, 
                         f"{horario.hora_inicio} - {horario.hora_fin}", 
                         horario.get_dia_semana_display()])
    
    return response

def reporte_por_grupo(request, grupo_id):
    horarios = Horario.objects.filter(materia_grupo_id=grupo_id, activo=True)
    
    # Crear la respuesta HTTP con el formato CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="reporte_grupo.csv"'
    
    # Crear el objeto writer de CSV
    writer = csv.writer(response)
    
    # Escribir los encabezados
    writer.writerow(['Docente', 'Aula', 'Hora', 'Día'])
    
    # Escribir los datos de cada horario
    for horario in horarios:
        writer.writerow([f"{horario.docente.nombre} {horario.docente.apellido_paterno}", 
                         horario.aula.clave, 
                         f"{horario.hora_inicio} - {horario.hora_fin}", 
                         horario.get_dia_semana_display()])
    
    return response
