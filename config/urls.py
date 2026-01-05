from django.contrib import admin
from django.urls import path, include  # Solo una vez

urlpatterns = [
    path('admin/', admin.site.urls),      # Rutas predeterminadas
    path('horarios/', include('horarios.urls')),  # Rutas de la app 'horarios'
]
