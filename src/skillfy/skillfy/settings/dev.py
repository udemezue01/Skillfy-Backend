from .base import *


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '@^_gf^z$l)5uz7eb*@gehkw@un*yfe_nkn3=u%k807s7e(!ye9'


ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

