# Setting Up A Tiny Blog

## Django Girls Project

- Setting up a virtual environment
Made a new directory in my system. Inside that installed the python virtual environment using the command **python3 -m venv <virtual-environment-name>**. That showed some error and thus, I had to install python virtual environment like this **sudo apt install python3-venv**. Then I deleted the entire directory, made the directory again using **mkdir <directory-name>**. Inside this directory, I ran the command **python3 -m venv <virtual-environment-name>**, after which I activated it by **source myvenv/bin/activate**.

- PIP should be up to date
This we ran the command *(myvenv) ~$ **python3 -m pip install --upgrade pip**. Everything done here onwards will have the name of the virtual env before the prompt inside the brackets.

- Creating the requirements file
We need Django, thus we ran the following two commands: **echo "Django~=2.0.6" > requirements.txt**, **pip install -r requirements.txt**. 

- Creating the project
Use command **django-admin startproject mysite .** (The dot at the end is important)

- Create the database
Use this command, **python manage.py migrate**

- Starting the web server
Use this command, **python manage.py runserver**

- Create tables for the newly created model in the database
Use command, **python manage.py makemigrations blog** (where *blog* is the name of the newly created model)
Then you need to apply the migration file to the database, use: **python manage.py migrate blog**

- Learn about [DJANGO MODEL REFERENCE](https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types)

- Learn about [DJANGO ADMIN](https://docs.djangoproject.com/en/2.0/ref/contrib/admin/)
- Learn about [DJANGO DEPLOYMENT CHECKLIST](https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/). These are important for maintaining the security issue of the application.

- Learn about [URLconf](https://docs.djangoproject.com/en/2.0/topics/http/urls/).

- Learn about [DJANGO Views](https://docs.djangoproject.com/en/2.0/topics/http/views/).

- CSS transitions [here](https://robots.thoughtbot.com/transitions-and-transforms).

- To make changes to the website, I first push the changes to this repo. Then I go the host server webpage and pull the changes to the respective directory. Then I reload the page.

- Learn about [query sets](https://docs.djangoproject.com/en/2.0/ref/models/querysets/#date). [Here](https://stackoverflow.com/questions/5245307/django-date-filter-gte-and-lte) is a good question regarding chaining similar type of queries by of different properties. Also check this out about [Django ORMs](https://www.fullstackpython.com/object-relational-mappers-orms.html).

- The static folder had problems rendering through PythonAnywhere. I had to change the default path of the /static/ url to the required directory and reload the app.

