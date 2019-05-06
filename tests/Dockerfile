FROM python:3.7-alpine

WORKDIR /usr/src/app

COPY requirements-dev.txt .

RUN pip install -r requirements-dev.txt

COPY . .

CMD python -m pytest -vv tests/
