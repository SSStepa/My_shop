FROM python:3.9
WORKDIR /usr/src/app
RUN python -m pip install Django
RUN python -m pip install psycopg2
RUN python -m pip install Pillow
RUN pip install django-mptt
RUN pip install django-bootstrap-v5
