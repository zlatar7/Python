# PROYECTO CODER

### Información

Es un proyecto realizado por un estudiante (Guido Zlatar) de programación en python para el sitio de e-learning "CoderHouse", cuyo objetivo es el aprendizaje de las herramientas proporcionas por el framework django.
Este proyecto se trata de un supuesto sitio web que ofrece capacitaciones a traves de clases virtuales.


### Navbar Options

##### Para usuarios no registrados

- Home
- About
- Login
- Register

##### Para usuarios registrados

- Edit (Interfaz de edición de blogs)
- Chat (Canal de mensajeria entre usuarios)
- Profile (Interfaz de edicion del perfil)
- Logout

#### AppCoder directory (paths)

- AppCoder/ (Página de inicio donde se observar, buscar (mediante formulario) e ingresar a los distintos posts)
- UserCoder/ (Página de registro e inicio de sesion )
- Chat/ (Página del canal de mensajeria )
- admin/ (Página de administración para el Superuser)

#### Paquetes instalados
- asgiref==3.5.2
- dj-database-url==1.0.0
- Django==4.1
- django-ckeditor==6.5.1
- django-js-asset==2.0.0
- gunicorn==20.1.0
- Pillow==9.2.0
- psycopg2==2.9.3
- sqlparse==0.4.2
- tzdata==2022.2
- whitenoise==6.2.0

(En el archivo requirements.txt se encuentran todos los paquetes instalados)

### Comandos en la consola (PowerShell)

Dentro de la carpeta Proyecto31095:

##### Activación del entorno virtual

- venv\Scripts\Activate.ps1 

##### Migraciones de los modelos

- python manage.py makemigrations
- python manage.py migrate

##### Correr el servidor

- python manage.py runserver
