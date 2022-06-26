# Creating a virtual environment
    py -m venv env

# Activating a virtual environment
    .\env\Scripts\activate

# Create a Project
    django-admin startproject crudexample  

# Create an App
    python manage.py startapp employee  

# Build Application Specific Port
    python manage.py runserver 100

# Build Model Migration to DB Start 
    python manage.py makemigrations
    python manage.py migrate
# Bu ild Model Migration to DB End

# Create User
    python manage.py createsuperuser