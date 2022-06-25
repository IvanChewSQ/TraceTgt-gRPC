#FROM gcr.io/google_appengine/python:latest
FROM python:3.9

#change to this working directory of 'app'
WORKDIR /app

ADD . /app

#copies requirements to "app"
COPY ./requirements.txt /app

#copies protos to "app"
COPY ./protos /app

#copies data.json to 'app'
COPY ./data/data.json /app

#copies location.json to 'app'
COPY ./data/cluster.json /app

#copies script to 'app'
COPY ./server.py /app
COPY ./database.py /app
COPY ./Tracetogether_pb2.py /app
COPY ./Tracetogether_pb2_grpc.py /app
COPY ./client.py /app
COPY ./client_moh.py /app
COPY ./login.py /app

RUN pip install --upgrade pip

#Install python Dependecies
RUN pip install --no-cache-dir -r requirements.txt --no-dependencies

ENTRYPOINT ["python", "-u", "server.py"]
