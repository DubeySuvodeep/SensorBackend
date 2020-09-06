from django.conf.urls import url
from django.urls import path

from .views import Sensor, SensorTypeDetail
                   
urlpatterns = [
    path('sensor-data/', Sensor.as_view(), 
        name='SensorData'),
    path('sensor-type/', SensorTypeDetail.as_view(), 
        name='SensorType'),
]