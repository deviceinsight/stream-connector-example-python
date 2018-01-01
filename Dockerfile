FROM python:3.6.4-alpine3.7

ADD stream-connector.py /usr/src/app/stream-connector.py

WORKDIR /usr/src/app

# Disable buffering
CMD [ "python", "-u", "./stream-connector.py" ]
