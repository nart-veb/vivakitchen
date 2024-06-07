import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'djaasdasd231nsecure21w3-z$#k==ur@0_21j@l&r3fsajpx+bfrus!(8u*el-*9q9&xfdwu=72!32tgfx'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'vivakitchen-sochi.ru', '185.233.187.168']


CSRF_TRUSTED_ORIGINS=['http://vivakitchen-sochi.ru']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'vivakitchen',
        'USER': 'nart',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}





STATIC_ROOT = os.path.join(BASE_DIR, "static")
