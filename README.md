# pyramid
Ejemplo de aplicación pyramid


Es aplicación posee un Login y un Home básico.


Requerimientos:
- python-virtualenv

Instalar la aplicación:
* Descargue el repositorio
* Active el virtualenv: source env/bin/activate
* Instalar los paquetes: pip install -e .
* Inicializar la base: initialize_db development.ini

El usuario creado por defecto es admin, con clave admin

Ejecutar la aplicacion: 
* Active el virtualenv: source env/bin/activate
* pserve development.ini --reload


Pasos que hice para realizar la aplicación:

* Crear el virtual env:
    python3 -m venv ./env

* Activarlo para instalar los paquetes necesarios:
    source env/bin/activate

* Instalar pyramid:
    (env) emanuel@emanuel:~/Documentos/pyramid$ pip install "pyramid==1.9.2" waitress

* Crear estructura básica pyramid:
    (env) emanuel@emanuel:~/Documentos/pyramid$ pip install cookiecutter
    (env) emanuel@emanuel:~/Documentos/pyramid$ cookiecutter gh:Pylons/pyramid-cookiecutter-starter --checkout 1.9-branch   
    project_name [Pyramid Scaffold]: pyramid-login
    repo_name [pyramid_login]: 
    Select template_language:
    1 - jinja2
    2 - chameleon
    3 - mako
    Choose from 1, 2, 3 [1]: 


    Change directory into your newly created project.
        cd pyramid_login

    Create a Python virtual environment.
        python3 -m venv env

    Upgrade packaging tools.
        env/bin/pip install --upgrade pip setuptools

    Install the project in editable mode with its testing requirements.
        env/bin/pip install -e ".[testing]"

    Run your project's tests.
        env/bin/pytest

    Run your project.
        env/bin/pserve development.ini

    (env) emanuel@emanuel:~/pyramid$ pip install -e .


* Crear base de datos Postgres (yo utilize la imagen de docker oficial de postgres)
    - docker run --name postgres -p 5432:5432 -e POSTGRES_PASSWORD=admin -d postgres
    - crear el usuario pyramid con clave my_password.
    - crear la base pyramid con el usuario antes creado



Documentación:

https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html