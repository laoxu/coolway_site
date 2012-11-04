# -*- encoding: utf-8 -*-
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'coolway',                      # Or path to database file if using sqlite3.
        'USER': 'coolway',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.    
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
    }
}

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_HOST='smtp.gmail.com'
#先通过gmail发送邮件、下面设置自己的账号密码
EMAIL_HOST_USER='51weekend@gmail.com'
EMAIL_HOST_PASSWORD=''
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'