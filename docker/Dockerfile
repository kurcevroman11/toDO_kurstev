FROM python:alpine3.19


RUN mkdir /web_django

WORKDIR /web_django

COPY requirements.txt /web_django/

RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /web_django/

RUN python manage.py migrate

RUN echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpassword')" | python manage.py shell

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
