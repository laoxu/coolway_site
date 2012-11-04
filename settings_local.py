DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'coolway',                      # Or path to database file if using sqlite3.
        # 'USER': 'root',                      # Not used with sqlite3.
        # 'PASSWORD': 'cdggcdgg',                  # Not used with sqlite3.
        # 'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.    
        'PORT': '3306',                      # Set to empty string for default. Not used with sqlite3.
        'USER': 'admin',                      # Not used with sqlite3.
        'PASSWORD': 'sfvxvi32$asv',                  # Not used with sqlite3.
        'HOST': '42.121.89.124', 
    }
}

DEFAULT_FROM_EMAIL = "noreply@coolway.com"

ACCOUNT_ACTIVATION_DAYS = 7

EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER='51weekend@gmail.com'
EMAIL_HOST_PASSWORD='cdggcdgg!82'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'