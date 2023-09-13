# Setting up the Django project 2023
# Open Project
- cd littlelemon (directory to manage.py file)
- python3 manage.py runserver
- http://127.0.0.1:8000(by default)
- setup your DB
- DATABASES = {
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'littlelemon',
    'USER': '--add here--',
    'PASSWORD': '--add here--',
    'HOST': '127.0.0.1',
    'PORT': '3306',
    'OPTIONS': {
      'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
      }
    }
}

- Compose a back-end application using multiple skills.
- Use Django to serve static HTML content.
- Commit the project to a Git repository.
- Set up the MySQL connection, and create the required models for the web application.
- Working with databases and models in Django.
- Set up user registration and authentication.
- Test the application with unit tests and Insomnia/Postman.

# Create a Python virtual environment, activate it and install Django in it:

- The macOS commands to activate virtual environment and install Django:
- pip install virtualenv
- python3 -m venv env
- source env/bin/activate
- which python (python3)

# Create project:

- pip3 install django
- django-admin startproject littlelemon

# Current directory to littlelemon and create a djangoapp with the name restaurant:

- cd littlelemon
- python3 manage.py startapp restaurant
- python3 manage.py runserver or python3 manage.py runserver (9000) - custom port :)

# Committing the Project:

- git add .
- git status
- git commit -m "add project"
- git push

# Setting up the MySQL connection:

- mysql -u root -p
- CREATE DATABASE littlelemon;
- SHOW DATABASES;
- CREATE USER 'root'@'localhost' IDENTIFIED BY 'gagik';
- GRANT ALL ON _._ TO 'root'@'localhost';
- FLUSH PRIVILEGES;
- ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'gagik';
- show grants for 'root'@'localhost';
- pip3 install mysqlclient
- python3 manage.py makemigrations
- python3 manage.py migrate

# Setting up the models:

- MenuItems
- Booking
- python3 manage.py makemigrations
- python3 manage.py migrate
- register the models in admin.py module
- python3 manage.py runserver

# Create superuser:

- python3 manage.py createsuperuser
  username: gagik
  email: gagik@project.com
  password: gagik

# Create Django Rest Framework(DRF)

- The Django REST Framework (DRF) acts as a wrapper around the core Django library. It serializes the view response into JSON format and returns it to the client.
- Recall that the process of serialization involves converting the model instances to native Python datatypes so that they can be rendered into JSON format.
- Deserialization parses the data back into the model instance after first validating the incoming data.
- pip3 install djangorestframework
- add 'rest_framework', in settings.py/ INSTALLED_APPS

# Set up the table booking API:

- DRF's browsable API feature makes it possible to send HTTP methods through the browser.
- The routes mapped to the ViewSets are registered with the router at the project level, so the need for setting up the routes in the app's urlpatterns is eliminated.
- Define a view, require a single class inheriting the ViewSet class that can handle GET, POST, PUT and DELETE requests.

# Add the registration page:

- pip3 install djoser (authentication library)
- 'djoser' to the INSTALLED_APPS list in the settings.py file.
- python3 manage.py makemigrations
- python3 manage.py migrate

# Create new user whit token:

- used the djoser library to implement registration, login, and logout features.

- using: http://127.0.0.1:8000/admin/auth/user/add/
  login: mike
  password: 123lemon
- To login, visit the djoser generated URL http://127.0.0.1:8000/auth/token/login/:
  enter the username and password to obtain the token.

# Securing the table booking API:

- The HTTP client passes this token in the request header. You can then restrict a view only for authenticated users.

# Unit Testing:

- create folder: tests
- create file 'test_models.py' and view test in 'test_views.py'
- python3 manage.py test

# Insomnia tools:

- Select the POST HTTP method to send the request.
- Check whether the response contains 201 CREATED status code.
- Enter the correct URL.
- Enter the fields and their values in the body tab in JSON format.

## CHECK II OUT:

# Login http://127.0.0.1:8000/admin/

whit:
username: gagik
email: gagik@project.com
password: gagik

- http://127.0.0.1:8000/restaurant/menu-items
- http://127.0.0.1:8000/restaurant/menu-items/1
- http://127.0.0.1:8000/auth/users/
- http://127.0.0.1:8000/auth/token/login/
- http://127.0.0.1:8000/auth/token/logout/

