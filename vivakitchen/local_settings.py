from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'djaasdasd231nsecure21w3-z$#k==ur@0_21j@l&r3fsajpx+bfrus!(8u*el-*9q9&xfdwu=72!32tgfx'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]

