FROM python:3.7

WORKDIR /opt/basic_restapi_testfwk
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /opt/basic_restapi_testfwk
