# M5

## Comandos:

### Ambiente virtual:
```
    python -m venv venv
    .\venv\Scripts\Activate.ps1
    deactivate
```

### Dependências da aplicação:

```
    pip freeze
    pip install djangorestframework black ipython
    pip freeze > requirements.txt
```

### Inicie a estrutura de um projeto Django

```
    django-admin startproject nome_do_diretorio_django .
```

### Iniciando um app:

```
    python manage.py startapp nome_do_app
```

### Iniciando o servidor:

```
    python manage.py runserver
```

### Migrations:

```
    python manage.py makemigrations
    python manage.py migrate
```
