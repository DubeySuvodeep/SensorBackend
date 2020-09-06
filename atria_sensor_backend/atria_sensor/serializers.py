import os

from django.conf import settings
from rest_framework import serializers

from .models import SensorType

class SensorSerailizer(serializers.Serializer):

    reading = serializers.FloatField(required=False)
    timestamp = serializers.IntegerField(required=False)
    sensor_type = serializers.CharField(required=False)


class RequestDataSerializer(serializers.Serializer):

    start_date = serializers.CharField(required=False, allow_null=True)
    end_date = serializers.CharField(required=False, allow_null=True)
    sensor_type = serializers.CharField(required=False, allow_null=True)


class SensorTypeReadSerializer(serializers.ModelSerializer):

    class Meta:
        model = SensorType
        fields = '__all__'

