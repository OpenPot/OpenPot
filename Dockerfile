FROM python:3.8-alpine

ENV INSTALL_PATH /openpot
RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY /config ${INSTALL_PATH}/config
COPY /openpot ${INSTALL_PATH}/openpot

CMD gunicorn -b 0.0.0.0:80 --access-logfile - "openpot.app:create_app()"
