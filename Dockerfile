FROM python:3.8-alpine

ENV SOURCE_PATH /openpot
ENV INSTALL_PATH /openpot
RUN mkdir -p ${INSTALL_PATH}
WORKDIR ${INSTALL_PATH}

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ${SOURCE_PATH} ${INSTALL_PATH}

CMD gunicorn -b 0.0.0.0:80 --access-logfile - "app:app"
