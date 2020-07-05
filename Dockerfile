
FROM python:3

RUN mkdir -p /usr/src/ghiblimovies
ADD . /usr/src/ghiblimovies
# to delete after dev
RUN mkdir -p /ghiblimovies
ADD . /ghiblimovies
WORKDIR /usr/src/ghiblimovies

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# some projects vars
ENV PORT=8000
ENV HOME /usr/src/ghiblimovies/

RUN apt-get update && apt-get install -y --no-install-recommends \
	    tzdata \
        python3-setuptools \
        python3-pip \
        python3-dev \
        python3-venv \
        gunicorn \
		postgresql-client libpq-dev \
        python-gdal python-psycopg2 \
        python-dev libgdal-dev gcc musl-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# install environment dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade --no-cache-dir --src /usr/src -r requirements.txt

RUN chmod a+x /usr/src/ghiblimovies/entrypoint.sh

#WORKDIR /usr/src/ghiblimovies/
WORKDIR /ghiblimovies
