# Campus Connect 
### Django Backend

[Python 3.5.2](https://www.python.org/downloads/release/python-352/)
## Modules
Django - `pip install Django` 
Rest Framework - `pip install djangorestframework`

## First time running
`python manage.py migrate` 
`python manage.py createsuperuser`

## Starting the server
`python manage.py runserver`

## Testing API commands
`curl --data "login=<your_login>&password=<your_password>"  http://127.0.0.1:8000/api-token-auth/`
