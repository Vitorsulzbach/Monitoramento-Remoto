FROM ubuntu:18.04
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
RUN apt-get update
RUN apt-get -y install libc-dev
RUN apt-get -y install build-essential
RUN apt-get -y install apt-utils
RUN apt-get -y install python3.6
RUN apt-get -y install python3.6-dev
RUN apt-get -y install python3-pip
RUN apt-get -y install python3-psycopg2
COPY requirements.txt /code/
RUN pip3 install -r requirements.txt
RUN apt-get -y install vim
RUN mkdir workspace
