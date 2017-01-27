#!bin/bash


echo "Installing requirements"
pip install -r requirement.txt

echo "Creating migrtations"
python manage.py syncdb

echo "Creating tables"
python manage.py migrate
