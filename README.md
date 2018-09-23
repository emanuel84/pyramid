# pyramid
Ejemplo de aplicación pyramid


Es aplicación posee un Login y un Home básico.


Requerimientos:
- python-virtualenv


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

    ===============================================================================
    Documentation: https://docs.pylonsproject.org/projects/pyramid/en/latest/
    Tutorials:     https://docs.pylonsproject.org/projects/pyramid_tutorials/en/latest/
    Twitter:       https://twitter.com/PylonsProject
    Mailing List:  https://groups.google.com/forum/#!forum/pylons-discuss
    Welcome to Pyramid.  Sorry for the convenience.
    ===============================================================================

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





Documentación:

https://docs.pylonsproject.org/projects/pyramid/en/latest/quick_tutorial/index.html