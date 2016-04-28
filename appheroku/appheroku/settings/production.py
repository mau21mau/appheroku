from appheroku.settings.base import *

DEBUG = False
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql',
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'sqlite3.db'),
        #'NAME': 'olist',
        #'USER': 'olist',
        #'PASSWORD': 'master',
        #'HOST': '127.0.0.1',
        #'PORT': '5432',
    }
}
