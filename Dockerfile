FROM python:3.9
WORKDIR /usr/src/app
RUN pip install Django psycopg2 django-bootstrap-v5 django-mptt Pillow
