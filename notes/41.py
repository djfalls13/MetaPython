
######## Django Project Setup Notes  #########

# Create Virtual Environment
$python3 -m venv app_name

# Activate Virtual Environment
$source app_name/bin/activate      #type deactivate to exit

# Install Django
$pip3 install Django

# Create Project.  Make sure to include '.' at the end
$django-admin startproject app_name .

# Create the Database
$python3 manage.py migrate

# Run / Test the Server
$python3 manage.py runserver

# Starting an App in another terminal while Server is running
	# Enter Virtual Env again in same directory as manage.py
	$source app_name/bin/activate
	# Tell Django to create infrastructure to build an App
	$python manage.py startapp app1 # unique name different from Project Name
	#Create Models      # List of Django Models at https://docs.djangoproject.com/en/1.10/ref/models/fields/
	$nano app1/models.py  #or open in PyCharm

# Activate App Model in main project directory in Settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #My Apps
    'app1',
]

	# Tell Django to update the Database
	$ python3 manage.py makemigrations learning_logs
	$ python3 manage.py migrate

# Prepare to Administer Site by creating the Super User to manage the site Models
$ python3 manage.py createsuperuser

# Default Models like Groups or Users are already included, but Custom Models must be registered in admin.py
	from django.contrib import admin

	# Register your models here.

	from app1.models import App1  #Class Name

	admin.site.register(App1)

# Login to http://127.0.0.1:8000/admin/ to manage Models

# Review data in Django Shell
$ python3 manage.py shell  # stuff

# Define URLs in main projects folder URLs.py file
	from django.conf.urls import url
	from django.contrib import admin

	urlpatterns = [
	    url(r'^admin/', admin.site.urls),
	    url(r'', include('learning_logs.urls', namespace='learning_logs')), # added line
	]
	# Add a urls.py file in the app directory that this points to. 
	from django.conf.urls import url
	from . import views

	urlpatterns = [
	    # HomePage
	    url(r'^$', views.index, name='index'),
	]



