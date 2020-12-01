FROM ubuntu:18.04

RUN apt-get update \
 && apt-get -y install sudo

RUN apt-get install -y wget nginx python3 python3-pip iputils-ping

RUN pip3 install uwsgi django djongo sqlparse==0.2.4

COPY mangalist /app/mangalist

WORKDIR /app/mangalist/mysite

COPY config_files/mysite.conf /etc/nginx/sites-available/mysite.conf

RUN sudo ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf

RUN rm -f /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

RUN python3 manage.py collectstatic --noinput

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    /etc/init.d/nginx start && \
    uwsgi --socket :8001 --module mysite.wsgi

## start mongodb 
## mynet is a created network
## docker run -d -p 27017:27017 -v ~/data:/data/db --name mongo --network mynet mongo
## build the image
## docker build -t mangalist --network mynet .
## start a container form the image
## docker run -d --network mynet mangalist