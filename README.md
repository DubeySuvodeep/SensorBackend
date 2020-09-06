# SensorBackend


1. To start the project up and running<br/>
<code>sudo docker-compose up --build</code>


2. If properly build the project will run on 0.0.0.0:8000 and mongo will run on 0.0.0.0:27017<br/>
   Download a Mongo Client like Robo3T and create the following

3. Create a Database<br/>
<code>DB_NAME = 'Sensor'<code>

4. Create a Collection
<code>Collection_Name = 'sensor_all_data'</code>

5. Go to the django Conatiner and execute the script in the tests.py to populate the mongo with test data<br/>
   

