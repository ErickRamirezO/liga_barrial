## Crear entorno virtual de python
Primero se crea el entorno para que funcione de mejor forma Django
```python
py -m venv "nombre_environment" .
```

## Activar el virtual environment
```python
Scripts\activate.bat
```
Y nos debe salir algo como esto en consola
```bash
(nombre_environment) C:\Users\Your Name>
```
Esto quiere decir que estamos dentro de nuestro entorno virtual

> [!IMPORTANT]
> Mover todos los archivos dentro de la carpeta que se creó *nombre_environment*

## Instalar Django
```python
pip install django
```

## Correr Servidor 💻
Ingresamos a la carpeta liga, una vez dentro ejecutamos
```python
py manage.py runserver
```

Esto nos abrirá nuestro servidor en la dirección http://127.0.0.1:8000/

## Crear Aplicación en Django
Es una pagina web especifica de tu aplicacion, como el login, la pagina de inicio, registro, etc.
Cada módulo se lo crea con el siguiente comando:

```python
py manage.py startapp _nombre_modulo_
```

## Views
Funciones que hacen peticiones http como una pagina html.
> [!IMPORTANT]
> Si creamos una view debemos crear la url
```python
urlpatterns = [
    path('members/', views.members, name='members'),
]
```
> [!IMPORTANT]
> y en el archivo principal tambien debemos incluir la ruta

```python
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]
```

> [!NOTE]
> En settings en INSTALLED_APPS de la carpeta principal debemos incluir la carpeta o carpetas que hayamos creado por ejemplo login, dashboard, etc. De la siguiente manera.
```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'login',
    'dashboard'
]
```
Como vemos al final tenemos el login y el dashboard


## Modelos
Son para crear las bases de datos, por defecto Django usa SQLite.
Aqui creamos la base de datos como por ejemplo tenemos a Match

```python
class Match(models.Model):
title = models.CharField(max_length=100)
date = models.DateField()
location = models.CharField(max_length=100)
description = models.TextField()
```

Si creamos el modelo debemos usar el comando para que se actualice la base de datos
```python
py manage.py makemigrations _nombre_modulo_
```
En la carpeta migrations podemos ver el codigo fuente de la creacion de la base de datos pero no está aún creada para ello usamos:
```python
py manage.py migrate
```

## Crear usuarios
Django ya provee de un servicio propio para crear superusuarios dentro de la base de datos por defecto y se lo crea de la siguiente manera:
```python
py manage.py createsuperuser
```
Con esto ya podemos hacer uso de la página principal del login
