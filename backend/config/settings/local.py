from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "tennis_db",
        "USER": "tennis_user",
        "PASSWORD": "strongpassword",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
