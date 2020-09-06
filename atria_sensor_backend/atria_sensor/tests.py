import random
from django.test import TestCase
from .mongo import insert_one_doc_to_mongo
# Create your tests here.

def create_test_data():
    t=1593561600
    while t<=1598918400:
        reading = random.randint(20,30)
        insert_one_doc_to_mongo(
            'Sensor', 
            'sensor_all_data', 
            {
                'reading': reading,
                'timestamp':t, 
                'sensor_type': 'Temperature' if reading%2==0 else 'Rain'
            }
        )
        t += 3600
    return True