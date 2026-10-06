# Catálogo Django REST Framework

API REST para la gestión de catálogo de productos y consumo de servicios externos.

## Requisitos previos

- Python 3.10+
- Git

## Instalación y Configuración

1. Clonar el repositorio: https://github.com/danielsegundodev-bot/catalogo-django
   ```bash
   git clone 
   cd catalogo-django

```

2. Crear y activar el entorno virtual:
```bash
python -m venv venv
# En Windows (Git Bash):
source venv/Scripts/activate

```


3. Instalar dependencias:
```bash
pip install -r requirements.txt

```


4. Aplicar migraciones:
```bash
python manage.py migrate

```


5. Iniciar el servidor:**
```bash
python manage.py runserver

```



## Endpoints Principales

* `GET / POST` -> `/api/productos/`
* `GET / PUT / DELETE` -> `/api/productos/<id>/`
* `GET` -> `/api/productos/disponibles/` *(Filtro ORM: productos activos con stock > 0)*
* `GET` -> `/api/externa/` *(Consumo de API pública con timeout y manejo de errores)*

## Ejecutar Pruebas Automáticas

```bash
python manage.py test
