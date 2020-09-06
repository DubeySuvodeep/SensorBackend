FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN mkdir /application
ADD . /application/
WORKDIR /application
RUN apk add mariadb-dev && \
    apk add --no-cache jpeg-dev zlib-dev && \
    apk add --no-cache --virtual .build-deps build-base linux-headers gcc musl-dev libjpeg-turbo libpng-dev libjpeg-turbo-dev librdkafka-dev && \
    pip install -r requirements.txt
WORKDIR /application/atria_sensor_backend/
CMD ["python","manage.py","migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]