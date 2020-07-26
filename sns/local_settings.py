import os 

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'oh@@!2i!wruo^paa9c27je4y(n$$7*$3f2=_uk(jst8rsgtc(5'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'assy3',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1',
        'POST': '5432',
    }
}

DEBUG = True