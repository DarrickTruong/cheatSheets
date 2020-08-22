pip3 freeze > requirements.txt # in the back_end folder. saves a text file with the requirements of project

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