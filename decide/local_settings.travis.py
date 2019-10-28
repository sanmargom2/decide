language: python 
python: 
- "3.6"
env: 
- DJANGO=2.0 DB=postgres
before_install: 
- cd decide
install: 
- pip install -r ../requirements.txt
script: 
- python manage.py test
services:
  - postgresql

before_script:
 - psql -c "create user decide with password 'decide'" 
 - psql -c "create database decide owner decide"
 - python manage.py migrate
