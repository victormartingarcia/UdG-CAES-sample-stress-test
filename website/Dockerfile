FROM python:3.7-slim

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY . /website
WORKDIR /website

RUN apt-get update && \
    apt-get -y install netcat gcc

RUN python3 -m pip install -r requirements.txt

# run entrypoint.sh
ENTRYPOINT ["/website/entrypoint.sh"]