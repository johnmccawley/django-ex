# Django sample app on Digital Garage!

[Django](http://www.djangoproject.com) is a high-level Python Web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.

## Why Django?

With Django, you can take Web applications from concept to launch in a matter of hours. Django takes care of much of the hassle of Web development, so you can focus on writing your app without needing to reinvent the wheel. It’s free and open source.
### Ridiculously fast.
Django was designed to help developers take applications from concept to completion as quickly as possible.
### Fully loaded.
Django includes dozens of extras you can use to handle common Web development tasks. Django takes care of user authentication, content administration, site maps, RSS feeds, and many more tasks — right out of the box.
### Reassuringly secure.
Django takes security seriously and helps developers avoid many common security mistakes, such as SQL injection, cross-site scripting, cross-site request forgery and clickjacking. Its user authentication system provides a secure way to manage user accounts and passwords.
### Exceedingly scalable.
Some of the busiest sites on the planet use Django’s ability to quickly and flexibly scale to meet the heaviest traffic demands.
### Incredibly versatile.
Companies, organizations and governments have used Django to build all sorts of things — from content management systems to social networks to scientific computing platforms.

## Bootstrapping your Django Application.
This is a  project that you can use as the starting point to develop your own and deploy it on the [Digital Garage](http://thedigitalgarage.io). In this brief tutorial we are going combine Django with best practices in both application architecture and deployment, namely, Microservices and Linux Containers. We will bootstrap our Django application on the popular PaaS provider, Digital Garage. Digital Garage utilizes Red Hat Openshift, Google Kubernetes and Docker Containers to create an open and efficient way to incorporate these best practices into our project.

### Prerequisites
+ A Github account. If you do not already have a Github account, you can follow [this link](https://github.com/join?source=header-home) to sign up for free.
+ A Digital Garage Account. If you do not already have a Digital Garage account, you can sign up for free at [www.thedigitalgarage.io](http://cochera.thedigitalgarage.io/free-signup).

### What has been done for you

This is a minimal Django 1.8 project. It was created with these steps:

1. Create a virtualenv
2. Manually install Django and other dependencies
3. `pip freeze > requirements.txt`
4. `django-admin startproject project .`
3. Update `project/settings.py` to configure `SECRET_KEY`, `DATABASE` and `STATIC_ROOT` entries
4. `./manage.py startapp welcome`, to create the welcome page's app

From this initial state you can:
* create new Django apps
* remove the `welcome` app
* rename the Django project
* update settings to suit your needs
* install more Python libraries and add them to the `requirements.txt` file

### Special files in this repository

Apart from the regular files created by Django (`project/*`, `welcome/*`, `manage.py`), this repository contains:

```
django-ex
  ├── conf - all our configuration will be here
  │   └── reload.py
  ├── LICENSE
  ├── openshift - OpenShift-specific files
  │   ├── scripts - helper scripts
  │   │   └── run-in-container.sh
  │   └── templates - application templates
  │       ├── qs-django-postgresql.json - example template for Kubernetes.
  │       └── qs-django.json - example template for Kubernetes.
  ├── project
  │   ├── __init.py__
  │   ├── database.py
  │   ├── settings.py
  │   └── urls.py
  ├── welcome - application files
  │   ├── migrations
  │   │   ├── __init__.py
  │   │   └── 00001_initial.py
  │   └── templates - application templates
  │       ├── __init__.py
  │       ├── admin.py
  │       ├── database.py
  │       ├── models.py
  │       ├── tests.py
  │       └── views.py
  ├── requirements.txt   - list of dependencies
  ├── manage.py
  └── wsgi.py
```
## Deploying to Digital Garage via the web console.

We will be:

+ Forking the Django seed project on the Digital Garage Github Organization to your private repository.
+ Creating a Django application workspace on the Digital Garage platform.
+ Bootstrapping Django in your Digital Garage project/workspace with the PostgreSQL container from Docker Hub.
+ Building the application from the source in the forked repository and deploying the application to Digital Garage.

After signing into your Github account, go to: [www.github.com/thdigitalgarage/mean-ex](www.github.com/thedigitalgarage/django-ex) and fork the repository into your own account. This repository contains some files and a file structure that will give you a quick start on your Django application. I go into more detail on the files and file structure a little further into the tutorial. For now, let's complete our setup by logging into your Digital Garage account and set up our application.

After signing into your Digital Garage account, Choose the Add to Project link in the top menu bar to go to the template catalog.

![Add To Project](http://assets-digitalgarage-infra.apps.thedigitalgarage.io/images/screenshots/add_to_project.png)

In the add to project screen, choose the Django + PostgreSQL Quickstart (qs-django-postgresql) from the catalog.

![Add To Project](http://assets-digitalgarage-infra.apps.thedigitalgarage.io/images/screenshots/choose_quickstart.png)

In the template configuration page for the Django + PostgreSQL Quickstart change the Git Repository URL to point to the repository that was just forked into your account. `https://github.com/johnmccawley/django-ex.git`. If you are running this tutorial in the free Hello World tier, you will want to set the `Memory Limit` for PostgreSQL to 128Mi rather than the default 192Mi. This will give your application enough room to build and deploy all of the containers it needs. For the rest of the parameters, you can simply accept the defaults for the remaining parameters and click "Create"

![Add To Project](http://assets-digitalgarage-infra.apps.thedigitalgarage.io/images/screenshots/quickstart-configure-django-psql.png)

That's it. Digital Garage is now setting up your Django application. On the next page you'll be presented with some information about your new application. When you are ready, click "Continue to Overview". You will be taken to the Project Overview screen where you can watch Digital Garage do the setup work for you. In just a few minutes you'll have full Django application running in containers and managed through Google Kubernetes. When the application services and pods are completely deployed, (the pod status circle is Green) simply click on the application URL in the upper right corner of the overview screen. You will be taken to a browser to see a simple "Hello World" message.

## Bootstrapping your application via the Command-Line-Interface (CLI)

You can create a new application using the web console or by running the `oc new-app` command from the CLI. With the  Digital Garage CLI there are three ways to create a new application, by specifying either:

- [With source code](http://docs.thedigitalgarage.io/dev_guide/new_app.html#specifying-source-code)
- [Via templates](http://docs.thedigitalgarage.io/dev_guide/new_app.html#specifying-a-template)
- [DockerHub images](http://docs.thedigitalgarage.io/dev_guide/new_app.html#specifying-an-image)

### Using an application template

The directory `openshift/templates/` contains application templates that you can add to your Digital Garage project with:

    oc create -f openshift/templates/<TEMPLATE_NAME>.json

The template `django.json` contains just a minimal set of components to get your Django application into Digital Garage.

The template `django-postgresql.json` contains all of the components from `django.json`, plus a PostgreSQL database service and an Image Stream for the Python base image. For simplicity, the PostgreSQL database in this template uses ephemeral storage and, therefore, is not production ready.

After adding your templates, you can go to your Digital Garage web console, browse to your project and click the create button. Create a new app from one of the templates that you have just added.

Adjust the parameter values to suit your configuration. Most times you can just accept the default values, however you will probably want to set the `GIT_REPOSITORY` parameter to point to your fork and the `DATABASE_*` parameters to match your database configuration.

Alternatively, you can use the command line to create your new app, assuming your Digital Garage deployment has the default set of ImageStreams defined.  Instructions for installing the default ImageStreams are available [here](https://docs.openshift.org/latest/install_config/imagestreams_templates.html).  If you are defining the set of ImageStreams now, remember to pass in the proper cluster-admin credentials and to create the ImageStreams in the 'openshift' namespace:

    oc new-app openshift/templates/django.json -p SOURCE_REPOSITORY_URL=<your repository location>

Your application will be built and deployed automatically. If that doesn't happen, you can debug your build:

    oc get builds
    # take build name from the command above
    oc logs build/<build-name>

And you can see information about your deployment too:

    oc describe dc/django-example

In the web console, the overview tab shows you a service, by default called "django-example", that encapsulates all pods running your Django application. You can access your application by browsing to the service's IP address and port.  You can determine these by running

   oc get svc


### Without an application template

Templates give you full control of each component of your application.
Sometimes your application is simple enough and you don't want to bother with templates. In that case, you can let Digital Garage inspect your source code and create the required components automatically for you:

```bash
$ oc new-app centos/python-35-centos7~https://github.com/thedigitalgarage/django-ex
imageStreams/python-35-centos7
imageStreams/django-ex
buildConfigs/django-ex
deploymentConfigs/django-ex
services/django-ex
A build was created - you can run `oc start-build django-ex` to start it.
Service "django-ex" created at 172.30.16.213 with port mappings 8080.
```

You can access your application by browsing to the service's IP address and port.


### Logs

By default your Django application is served with gunicorn and configured to output its access log to stderr.
You can look at the combined stdout and stderr of a given pod with this command:

    oc get pods         # list all pods in your project
    oc logs <pod-name>

This can be useful to observe the correct functioning of your application.


### Special environment variables

#### APP_CONFIG

You can fine tune the gunicorn configuration through the environment variable `APP_CONFIG` that, when set, should point to a config file as documented [here](http://docs.gunicorn.org/en/latest/settings.html).

#### DJANGO_SECRET_KEY

When using one of the templates provided in this repository, this environment variable has its value automatically generated. For security purposes, make sure to set this to a random string as documented [here](https://docs.djangoproject.com/en/1.8/ref/settings/#std:setting-SECRET_KEY).


### One-off command execution

At times you might want to manually execute some command in the context of a running application in Digital Garage.
You can drop into a Python shell for debugging, create a new user for the Django Admin interface, or perform any other task.

You can do all that by using regular CLI commands from Digital Garage.
To make it a little more convenient, you can use the script `openshift/scripts/run-in-container.sh` that wraps some calls to `oc`.
In the future, the `oc` CLI tool might incorporate changes
that make this script obsolete.

Here is how you would run a command in a pod specified by label:

1. Inspect the output of the command below to find the name of a pod that matches a given label:

        oc get pods -l <your-label-selector>

2. Open a shell in the pod of your choice. Because of how the images produced
  with CentOS and RHEL work currently, we need to wrap commands with `bash` to
  enable any Software Collections that may be used (done automatically inside
  every bash shell).

        oc exec -p <pod-name> -it -- bash

3. Finally, execute any command that you need and exit the shell.

The wrapper script combines the steps above into one. You can use it like this:

    ./run-in-container.sh ./manage.py migrate          # manually migrate the database
                                                       # (done for you as part of the deployment process)
    ./run-in-container.sh ./manage.py createsuperuser  # create a user to access Django Admin
    ./run-in-container.sh ./manage.py shell            # open a Python shell in the context of your app

If your Django pods are labeled with a name other than "django", you can use:

    POD_NAME=name ./run-in-container.sh ./manage.py check

If there is more than one replica, you can also specify a POD by index:

    POD_INDEX=1 ./run-in-container.sh ./manage.py shell

Or both together:

    POD_NAME=django-example POD_INDEX=2 ./run-in-container.sh ./manage.py shell


### Data persistence

You can deploy this application without a configured database in your Digital Garage project, in which case Django will use a temporary SQLite database that will live inside your application's container, and persist only until you redeploy your application.

After each deploy you get a fresh, empty, SQLite database. That is fine for a first contact with Digital Garage and perhaps Django, but sooner or later you will want to persist your data across deployments.

To do that, you should add a properly configured database server. Then use `oc env` to update the `DATABASE_*` environment variables in your DeploymentConfig to match your database settings.

Redeploy your application to have your changes applied, and open the welcome page again to make sure your application is successfully connected to the database server.

## Local development

### Warnings

Please be sure to read the following warnings and considerations before running this code on your local workstation, shared systems, or production environments.

#### Database configuration

The sample application code and templates in this repository contain database connection settings and credentials that rely on being able to use sqlite.

#### Automatic test execution

The sample application code and templates in this repository contain scripts that automatically execute tests via the postCommit hook.  These tests assume that they are being executed against a local test sqlite database. If alternate database credentials are supplied to the build, the tests could make undesirable changes to that database.


To run this project in your development machine, follow these steps:

1. (optional) Create and activate a [virtualenv](https://virtualenv.pypa.io/) (you may want to use [virtualenvwrapper](http://virtualenvwrapper.readthedocs.org/)).

2. Fork this repo and clone your fork:

    `git clone https://github.com/openshift/django-ex.git`

3. Install dependencies:

    `pip install -r requirements.txt`

4. Create a development database:

    `./manage.py migrate`

5. If everything is alright, you should be able to start the Django development server:

    `./manage.py runserver`

6. Open your browser and go to http://127.0.0.1:8000, you will be greeted with a welcome page.
