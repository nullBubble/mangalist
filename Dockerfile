FROM ubuntu:18.04 as base

RUN apt-get update \
 && apt-get -y install python3 python3-pip

COPY reqs.txt . 

RUN pip3 install --user -r reqs.txt

FROM ubuntu:18.04

COPY --from=base /root/.local /root/.local

COPY --from=base /usr/lib/x86_64-linux-gnu/libpython3.6m.so.1.0 /usr/lib

RUN apt-get update \
&& apt-get -y install python3 nginx

ENV PATH=/root/.local/bin:$PATH

COPY . /app/mangalist

WORKDIR /app/mangalist/mysite

RUN rm -f /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default

COPY config_files/mysite.conf /etc/nginx/sites-available/mysite.conf

RUN ln -s /etc/nginx/sites-available/mysite.conf /etc/nginx/sites-enabled/mysite.conf

RUN python3 manage.py collectstatic --noinput

CMD python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    /etc/init.d/nginx start && \
    uwsgi --socket :8001 --module mysite.wsgi

## start mongodb 
## mynet is a created network with docker network create mynet
## docker run -d -p 27017:27017 -v ~/data:/data/db --name mongo --network mynet mongo
## build the image
## docker build -t mangalist --network mynet .
## start a container form the image
## docker run -d --network mynet nullbubble/mangalist:tag
