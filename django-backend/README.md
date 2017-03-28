# Campus Connect's Django Backend

[Programs and Modules to install](#Programs and Modules to install)  
[First time running](#first-time-running)  
[Starting the server](#starting-the-server)  
[Modifying the database](#modifying-the-database)  
[Testing API commands](#testing-api-commands)  
[Loggin In](#logging-in)  
[Future stuff to add](#future-stuff-to add)  


## Programs and Modules to install

[Python 3.6.1](https://www.python.org/downloads/release/python-361/)

Django - `pip install Django`  
Rest Framework - `pip install djangorestframework`  
Rest Documentation - `pip install coreapi`  
Docutils - `pip install docutils`

All: `pip install Django djangorestframework coreapi docutils`


## First time running
`python manage.py migrate`  
This will generate the database.

`python manage.py createsuperuser`  
This will create a super user, which has full access to edit everything on the site using http://127.0.0.1:8000/admin/


## Starting the server
`python manage.py runserver`

## Modifying the database
Navigate to [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/) login with the superuser you've created.

## Testing API commands
Navigate to [http://127.0.0.1:8000/rest-api/](http://127.0.0.1:8000/rest-api/)

## Logging in
Logging in requires retrieving a token, then storing it and using it for future API requests that need it.  
`curl --data "username=<user>&password=<password>" http://127.0.0.1:8000/token/`

## Future stuff to add
 * Registering using the API
 * Having the token be dynamic; being generated every time you login and being destroyed when logging out or after a certain amount of time.