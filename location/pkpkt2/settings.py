TIME_ZONE = 'America/Los_Angeles'

INSTALLED_APPS = (
    'location',
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}