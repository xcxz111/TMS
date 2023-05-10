#!/bin/sh

python manage.py makemigrations
python manage.py migrate
python manage.py createcachetable

if [ -n "$DJANGO_SUPERUSER_USERNAME" ] && [ -n "$DJANGO_SUPERUSER_PASSWORD" ] && [ -n "$DJANGO_SUPERUSER_EMAIL" ]
then
  python manage.py createsuperuser \
    --no-input \
    --username $DJANGO_SUPERUSER_USERNAME \
    --email $DJANGO_SUPERUSER_EMAIL ||echo "Failed to create createsuperuser"
else
  echo "One  or more of the required env variables not specified"
fi

python manage.py runserver 0.0.0.0:8000

