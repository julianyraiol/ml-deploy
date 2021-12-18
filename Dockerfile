FROM python:3.8-slim-buster

ARG USERNAME
ARG PASSWORD

ENV BASIC_AUTH_USERNAME = $USERNAME
ENV BASIC_AUTH_PASSWORD = $PASSWORD

WORKDIR /usr

RUN pip install --upgrade pip
COPY requirements.txt /usr/requirements.txt
RUN pip3 install -r requirements.txt

COPY ./src/ /usr/src
COPY ./models /usr/models

ENTRYPOINT [ "python3" ]
CMD [ "src/app/api.py" ]
