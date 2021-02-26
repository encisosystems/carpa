FROM python:3.8

RUN apt-get update

# For localizations
RUN apt-get install gettext -y; apt-get --assume-yes install binutils libproj-dev gdal-bin python3-gdal

# Setup workdir
RUN mkdir /src
WORKDIR /src

# Python dependencies
COPY requirements.txt /src/
RUN pip install -r /src/requirements.txt

# Test dependencies
COPY test-requirements.txt /src/
RUN pip install -r /src/test-requirements.txt

COPY . /src
