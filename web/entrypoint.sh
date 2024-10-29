#!/bin/sh

echo "entrypoint: Run web"

until nc -z $DB_HOST $DB_PORT; do
    sleep 1
done
echo "entrypoint: Database is up"

gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000