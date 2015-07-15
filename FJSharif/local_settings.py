# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases
import os
from FJSharif.settings import BASE_DIR

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'tempdb'),
    }
}