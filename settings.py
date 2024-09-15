INSTALLED_APPS = ['mydb']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'spiderweb.db',  # use the default spiderweb.db file
    }
}