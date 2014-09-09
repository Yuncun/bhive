DEBUG = True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'bhive',
        'HOST': 'localhost',
        'PORT': '5432',
        'USER': 'bhive',
        'PASSWORD': 'garbage',
        'OPTIONS': {'autocommit': True},
    }
}