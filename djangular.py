pip3 freeze > requirements.txt # in the back_end folder. saves a text file with the requirements of project

# in settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.flights', #import apps
    'rest_framework', #import rest_framework for api
    'corsheaders', #import cors for api
]


# in apps/app name/apps.py
from django.apps import AppConfig
class SchedulerConfig(AppConfig):
    name = 'scheduler'


# rest_frameworks router
# in apps/app name/urls.py
from django.conf.urls import url, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    # url(r'^$', views.index),
    url(r'', include(router.urls))
]

# in apps/app name/serializers.py
from django.contrib.auth.models import User
from apps.flights.models import Schedule
from rest_framework import serializers # allows complex data such as querysets and model instances to be converted
                                       # to native python datatypes that can be easily rendered into JSON and XML, etc

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = User
        fields = ('url', 'username', 'email')

class Schedule(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Schedule
        fields = (
            'airlines',
            'flight_no',
            'trip_type',
            'departure_airport',
            'arrival_airport',
            'departure_date',
            'return_date'
        )

# in apps/app name/views.py
from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from apps.flights.serializers import UserSerializer
from rest_framework import viewsets

def index(request):
    return HttpResponse("this is the equivalent of @app.route('/')!")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer



# Create admin/super user
python3 manage.py createsuperuser

django3 - ASGI vs WSGI(older)
- ASGI - Asynchronous Server Gateway Interface
- Might need to install ASGI server helper(daphne)

# Asynchronous Execution:
# When a task is executed asynchronously, you can directly switch to another task before the previous has been
# completed. One task does not depend on the other.

# Synchronous Execution :
# When a task is executed synchronously, you wait for a task to be completed before moving on to another task.
# One task depends on the end of another.

# Callback
