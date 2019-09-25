FROM python:3.6

WORKDIR /var/www/FlaskApp
COPY ./data/app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /var/www/FlaskApp/src
CMD ["uwsgi", "--ini", "/var/www/FlaskApp/uwsgi.ini"]
