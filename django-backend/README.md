# Campus Connect's Django Backend

[Programs and Modules to install](#Programs and Modules to install)  
[First time running](#First time running)  
[Starting the server](#Starting the server)  
[Modifying the database](#Modifying the database)  
[Testing API commands](#Testing API commands)  
[Future stuff to add](#Future stuff to add)  


## Programs and Modules to install

[Python 3.5.2](https://www.python.org/downloads/release/python-352/)

Django - `pip install Django`

Rest Framework - `pip install djangorestframework`


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
Using login info to get the user token  
`curl --data "login=<your_login>&password=<your_password>"  http://127.0.0.1:8000/api/token/`

Listing the clubs (work in progress)  
`curl --data "" http://127.0.0.1:8000/api/clublist/`

## Future stuff to add
 * Registering using the API
 * Using the token to modify Clubs and the Calendar
 * Having the token be dynamic; being generated every time you login and being destroyed when logging out or after a certain amount of time.