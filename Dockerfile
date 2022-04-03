FROM python:3.8

LABEL author="dmitriyvasil@gmail.com"

ENV DJANGO_SETTINGS_MODULE=deutsch.settings
ENV DB_PASSWORD=root
ENV DB_NAME=deutsch
ENV DB_USER=root
ENV DB_PORT=3306
ENV DB_HOST=db
ENV DEBUG=True

RUN mkdir -p /app/static /app/venv
WORKDIR /app
COPY . /app

RUN python -m venv /app/venv && \
    /app/venv/bin/pip install -r /app/requirements.txt

CMD /app/venv/bin/python runserver.py