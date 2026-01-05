from django.urls import path
from . import views

urlpatterns = [
    path('docente/<int:docente_id>/', views.horarios_por_docente, name='horarios_por_docente'),
]

urlpatterns += [
    path('grupo/<int:grupo_id>/', views.horarios_por_grupo, name='horarios_por_grupo'),
]

urlpatterns += [
    path('reporte/docente/<int:docente_id>/', views.reporte_por_docente, name='reporte_por_docente'),
]

urlpatterns += [
    path('reporte/grupo/<int:grupo_id>/', views.reporte_por_grupo, name='reporte_por_grupo'),
]

