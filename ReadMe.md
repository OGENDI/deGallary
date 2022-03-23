# DeGallery

# author
Derick Ogendi
 
# Project descriotion
A gallery application to display great images.


# User story
As a user is able to:-
+ View different Images 
+ Click on a single photo to expand it and  also view the details of the image. The photo details  appears on a modal within the same route as the main page.
+ Search for different categories of photos. (e.g. Animal, Food)
+ Copy a link to the photo to share with  friends.
+ View photos based on the location location

## Technologies used
    * BackEnd: * Python - Django
    * FontEnd:  jinja2 , CSS,   Bootstrap
    * Database * PostgreSQL
    * Deployment * Heroku

## Installation / Setup instruction

## Cloning
* Open Terminal {Ctrl+Alt+T}

* git clone ``git@github.com:OGENDI/deGallary.git``

 + or
 git clone ``https://github.com/OGENDI/deGallary.git``

* cd DeGallery

* Vs code . or atom . based on the text editor you have.

### The application requires the following installations to operate 
* python3
* virtual environment - see more on how to install virtual on google
* heroku for online deployment.
#### Requirements
    * asgiref==3.5.0
    * backports.zoneinfo==0.2.1
    * beautifulsoup4==4.10.0
    * dj-database-url==0.5.0
    * Django==4.0.2
    * django-bootstrap-v5==1.0.11
    * django-heroku==0.3.1
    * gunicorn==20.1.0
    * Pillow==9.0.1
    * psycopg2==2.9.3
    * python-decouple==3.6
    * soupsieve==2.3.1
    * sqlparse==0.4.2
    * whitenoise==6.0.0
### Running the application
once in the cloned folder runt he following commands:-
 * #### create Django environnent
        $  python3 -m venv pip virtual -- creates the virtual for runnning your app      
        $ source virtual/bin/env  -- activate  the virtual
        $ pip install -r requirements.txt - this installs all dependecies necessary for app to run
* #### Setup Configurations and Databases
        $ python3 manage.py makemigrations gallery 

* #### Running the application
        $ python3 manage.py runserver

* #### Running the application
        $ python3 manage.py test personal_gallery

* #### Browse app
        $ 127.0.0.1:8000

## Known Bugs
* There are no known bugs currently but pull requests are allowed incase you spot a bug
* also incase you run it a bug feel free to add or contact

## Contact Information 

If you have any question or contributions and support, please email me at [ogendi18@gmail.com](ogendi18@gmail.com)

LinkedIn - [Derick Ogendi](https://www.linkedin.com/in/derick-ogendi/)


# Licence

Click to  [MIT License](Licence) view

 Copyright (c) 2022 | Derick Ogendi