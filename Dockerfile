FROM python:latest

ENV INSTALL_PATH /iot-controller
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY iot_controller.py iot_controller.py
COPY src src/
