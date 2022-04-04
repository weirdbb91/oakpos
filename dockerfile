FROM python:3.9-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

COPY . .
RUN apt-get -y update && apt-get install -y wget
RUN python3 -m pip install --upgrade pip
RUN pip install -r requirements.txt

ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

EXPOSE 8000