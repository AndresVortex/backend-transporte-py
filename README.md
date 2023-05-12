
# Ejecución del proyecto

## 1. Entorno virtual
    - Crear entrono virtual
    py -m venv venv
    - Activar entorno virtual
    .\venv\Scripts\activate

## 2. instalación de librerías con requirements.txt

    pip install -r requirements.txt

## 3. Modificar settings.py para conexión de base de datos

    Ir a la carpeta "transporte/transporte"
    Abrir el archivo "settings.py" y buscar la variable "DATABASE"
    modificar variables "name, user, password, host, port" de acuerdo a su base de datos

    Ejemplo: Archivo settings.py
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nombre-db',
        'USER': 'nombre usuario',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
    }


## 4. Hacer la migraciones de los modelos
    Ingresar a la carpeta transporte (principal), donde se encuentra el archivo manage.py
    py manage.py makemigrations

## 5. Correr las migraciones 
    py manage.py migrate

## 6. Correr servidor

    py manage.py runserver
 

# Librerías usadas

- Django: es un framework de alto nivel que fomenta el desarrollo rápido y el diseño limpio y pragmático
- Django rest framework:  es un potente y flexible conjunto de herramientas para construir APIs Web.
- psycopg2: Es la librería que nos ayuda a comunicarnos con la base de datos postgres
- django-cors-headers: nos ayuda a controlar los cors de una petición hecha por el cliente

# Proceso de desarrollo 
- Se trabajo con Django y Django rest framework enfocado a clases para tener un código mas organizado y escalable. nos permiten tener mayor flexibilidad al momento de manejar las solicitudes y respuestas http. También nos favorece en aplicar el principio de responsabilidad única donde la clase o modulo solo debe tener una sola responsabilidad.   