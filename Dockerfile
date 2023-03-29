FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /src
WORKDIR /src

RUN apt-get update
COPY requirements.txt /src/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /code/
