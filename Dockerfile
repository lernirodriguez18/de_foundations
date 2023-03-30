FROM python:3.9

COPY ./requeriments.txt /usr/src/app/requeriments.txt

WORKDIR /usr/src/app

RUN python -m pip install --upgrade pip
RUN pip install -r requeriments.txt
