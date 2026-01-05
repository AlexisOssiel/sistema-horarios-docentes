# Sistema de Gestión de Horarios para Docentes

## Descripción
Este sistema permite gestionar los horarios de los docentes, validando los traslapes de aula y docente, generando reportes por docente y por grupo.

## Requisitos

Para ejecutar este proyecto, necesitas tener **Python 3.x** y las siguientes librerías:

- Django
- Otros requerimientos en `requirements.txt`

## Instalación

1. **Clonar el repositorio**:
    ```bash
    git clone https://github.com/AlexisOssiel/sistema-horarios-docentes.git
    ```

2. **Instalar dependencias**:
    Navega al proyecto y ejecuta:
    ```bash
    pip install -r requirements.txt
    ```

3. **Aplicar migraciones**:
    ```bash
    python manage.py migrate
    ```

4. **Crear superusuario** para acceder al admin:
    ```bash
    python manage.py createsuperuser
    ```

5. **Levantar el servidor**:
    ```bash
    python manage.py runserver
    ```

6. **Acceder a la interfaz de administración** en:
    ```
    http://127.0.0.1:8000/admin/
    ```

## Funcionalidades

- **Gestión de docentes, periodos, aulas, y horarios.**
- **Validación de traslapes en horarios.**
- **Generación de reportes en formato CSV** por:
  - Docente
  - Grupo
