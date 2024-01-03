from .base import *


DEBUG = True


ALLOWED_HOSTS = ['*']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


CSRF_TRUSTED_ORIGINS = [
    'https://c5f6-2400-9700-21-ae41-f243-a3a7-a3b6-4f41.ngrok-free.app'
]
