from .base import *

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "pointstodefend_db",
        "USER": "tiagoquinteiro",
        "PASSWORD": "federeristhegoat",
        "HOST": "localhost",
        "PORT": "5432",
    }
}
