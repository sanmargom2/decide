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
services:
  - postgresql
addons:
  postgresql: "9.6"
global:
  - PGPORT=5432

before_script:
 - psql -c "create user decide with password 'decide'" 
 - psql -c "create database decide owner decide"
 - python manage.py migrate
ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

APIS = {
    'authentication': 'http://localhost:8000',
    'base': 'http://localhost:8000',
    'booth': 'http://localhost:8000',
    'census': 'http://localhost:8000',
    'mixnet': 'http://localhost:8000',
    'postproc': 'http://localhost:8000',
    'store': 'http://localhost:8000',
    'visualizer': 'http://localhost:8000',
    'voting': 'http://localhost:8000',
}

BASEURL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256

y lo copiamos con el nombre adecuado modificando el fichero .travis.yml tal como sigue:

...

before_script:
 - cp local_settings.travis.py local_settings.py
