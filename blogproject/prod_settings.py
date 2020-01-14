from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['http://whitejamer.pythonanywhere.com/']

SECRET_KEY = os.getenv('SECRET_KEY', 'secretkey')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USERNAME'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}