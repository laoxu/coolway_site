# -*- encoding: utf-8 -*-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'coolway',                      # Or path to database file if using sqlite3.
        'USER': 'admin',                      # Not used with sqlite3.
        'PASSWORD': 'sfvxvi32$asv',                  # Not used with sqlite3.
        'HOST': '42.121.89.124',                      # Set to empty string for localhost. Not used with sqlite3.    
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_HOST='smtp.exmail.qq.com'
EMAIL_PORT=25

DEFAULT_FROM_EMAIL = 'xinyun@coolway.me'
SERVER_EMAIL = 'xinyun@coolway.me'

EMAIL_HOST_USER='xinyun@coolway.me'
EMAIL_HOST_PASSWORD='hello1234'
EMAIL_USE_TLS = False
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'