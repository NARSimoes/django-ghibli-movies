#!/bin/bash

source $HOME/ghiblimovies.env

set -euo pipefail

WAIT_FOR_POSTGRES=${WAIT_FOR_POSTGRES:-true}

if [[ "$WAIT_FOR_POSTGRES" = true ]]; then
    DATABASE_URL=${DATABASE_URL:-postgres://admin:admin@database:5432/movies}

    # convert to connection string
    POSTGRES_URL=${DATABASE_URL%%\?*}
    POSTGRES_URL=${POSTGRES_URL/#postgres:/database:}


    # let postgres and other services to warm up....
    until psql $POSTGRES_URL -c '\q'; do
        >&2 echo "**** Postgres database is not available - sleeping"
        sleep 3
    done
fi

if [[ $# -ge 1 ]]; then
    exec "$@"
else
    echo "Applying migrations"

    # migrations
    python manage.py makemigrations
    python manage.py migrate

    echo "Starting server"

fi
    exec python manage.py runserver 0.0.0.0:8990
