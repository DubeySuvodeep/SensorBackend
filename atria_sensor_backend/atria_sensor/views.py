import json
from django.shortcuts import render
from django.conf import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .mongo import insert_one_doc_to_mongo, get_docs_by_query
from .serializers import SensorSerailizer, RequestDataSerializer, SensorTypeReadSerializer
from .models import SensorType

# Create your views here.
# 1593561600	Wednesday, 1 July 2020 00:00:00
# Start of month: 	1598918400	Tuesday, 1 September 2020 00:00:00

class Sensor(APIView):

    authentication_classes = ()
    permission_classes = ()

    def post(self, request, **kwargs):

        serializer = SensorSerailizer(data=request.data)

        if serializer.is_valid():
            try:
                insert_one_doc_to_mongo("Sensor", "sensor_all_data", serializer.data)
                return Response(status=status.HTTP_200_OK)
            except Exception as e:
                print("Insertion Failed")
                print(e)
                return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
            
    def get(self, request):

        serializer = RequestDataSerializer(data={
                'start_date':request.GET.get('start_date', None),
                'end_date':request.GET.get('end_date', None),
                'sensor_type':request.GET.get('sensor_type', None),
            }
        )
        
        if serializer.is_valid():
            query = self.create_query(serializer.data['start_date'], serializer.data['end_date'], serializer.data['sensor_type'])
            _doc_sensor_data = get_docs_by_query('Sensor', 'sensor_all_data', { '$and' : query })
            _time = []
            _reading = []
            for i in _doc_sensor_data:
                _time.append(i['timestamp'])
                _reading.append(i['reading'])
            get_time_series = { 'time': _time, 'reading': _reading , 'sensor_type': serializer.data['sensor_type']}
            return Response( { 'graph_data': get_time_series },status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def create_query(self, start_date, end_date, sensor_type):

        query = []

        if start_date!=None and int(start_date)!=0:
            query.append({ 'timestamp': { '$gte': int(start_date) } })
        if end_date!=None and int(end_date)!=0:
            query.append({ 'timestamp': { '$lte': int(end_date) } })
        if sensor_type!=None:
            query.append({ 'sensor_type': sensor_type })

        return query


class SensorTypeDetail(APIView):

    authentication_classes = ()
    permission_classes = ()

    def get(self, request):

        sensor_type = SensorType.objects.all()
        serializer = SensorTypeReadSerializer(sensor_type, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
