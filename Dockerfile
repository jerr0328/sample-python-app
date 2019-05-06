FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY . .

CMD python sample/main.py
