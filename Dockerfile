FROM ubuntu:16.04

MAINTAINER Shankar Lal "shankar.lal@aalto.fi"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev mysql-client

COPY ./requirements.txt /root/requirements.txt

RUN pip install -r /root/requirements.txt

COPY ./keyserver.py /root/keyserver.py

RUN chmod 775 /root/keyserver.py

COPY ./init-script.sh /root/init-script.sh

COPY ./secret.sql /root/secret.sql

RUN chmod 775 /root/init-script.sh

ENTRYPOINT /root/init-script.sh
