#!/bin/bash

sleep 1
echo "Reading CSV"
python djangoapp/read_csv_file.py
echo "==================================="

sleep 1
echo "Create migrations"
python manage.py makemigrations djangoapp
echo "==================================="


sleep 3
echo "Migrate"
python manage.py migrate 
echo "==================================="

sleep 3
echo "Loading Database"
python manage.py loaddata data.json
echo "==================================="

sleep 3
echo "Creating User"
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')"
echo Super User created: "{
    "username": "admin",
    "password": "adminpass"
}"
echo "==================================="

sleep 3
echo "Running Unit Tests"
python manage.py test
echo "==================================="

sleep 3
echo "Start Server"
python manage.py runserver 0.0.0.0:8000



