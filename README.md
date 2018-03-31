# Meal Planner
Web service that helps you plan out meals for the week or one meal at a time.

## Setup
Setup is minimal since the web service is run in a docker container.

## Development mode
In order to get a local web server running, simply navigate to the root folder and use the command `docker-compose up`. With the current settings, you should now be able to access the service via `localhost:8000` When you are finished developing, either navigate to the window and press `ctrl-C` or navigate to a different window and use `docker-compose down`.

Django commands must be prefixed with `sudo docker-compose run web` to run inside the container.

* `sudo docker-compose run web python manage.py startapp <app name>` will create a new Django app.
* `sudo docker-compose run web python manage.py makemigrations <app>` will create migrations for a new Django app.
* `sudo docker-compose run web python manage.py migrate` will apply these migrations.

Note: Newly created apps should have their group ownership changed via `sudo chown -R $USER:$USER .` in the root folder.
