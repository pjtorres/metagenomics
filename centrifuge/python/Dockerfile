FROM python:3.5

MAINTAINER Pedro J. Torres

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        libatlas-base-dev gfortran

# Make a new directory where I will keep all the requirements for pandas
RUN mkdir -p /opt/pandas/

#Copy requirements text in your current directory to the container at /opt/pandas/
COPY requirements.txt /opt/pandas/requirements.txt

RUN pip install -r /opt/pandas/requirements.txt
