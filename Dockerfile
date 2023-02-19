# https://hub.docker.com/_/python for any other docker image.

FROM python:3.11.2-alpine3.17

WORKDIR /ChatAPI

COPY ChatAPI/requirements.txt /ChatAPI/

RUN pip install --no-cache-dir -r requirements.txt

COPY ChatAPI /ChatAPI/

CMD ["/bin/bash", "/start-server.sh"]