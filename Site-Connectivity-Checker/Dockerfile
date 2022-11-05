FROM python:3.7-alpine

MAINTAINER Chris Allan Wajega

ENV PYTHONUNBUFFERED 1
COPY ./requirements.txt requirements.txt
RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /
COPY ./ /app


RUN adduser -D user
USER user
