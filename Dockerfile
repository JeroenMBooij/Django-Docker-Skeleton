FROM python:3.8 as base

RUN pip install pipenv
RUN pip install mysqlclient

ENV PYTHONUNBUFFERED=1
ENV PROJECT_DIR /usr/src

WORKDIR ${PROJECT_DIR}

COPY . ${PROJECT_DIR}/

RUN pipenv install --system --deploy