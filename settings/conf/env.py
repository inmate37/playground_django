# Third party
from decouple import (
    Csv,
    config
)


SECRET_KEY = config('SECRET_KEY', cast=str)
ENVIRONMENT = config('ENVIRONMENT', cast=str)
DEBUG = config('DEBUG', cast=bool)
ADMIN_PAGE_URL = config('ADMIN_PAGE_URL', cast=str)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_PORT = 587
EMAIL_HOST = config('EMAIL_HOST', cast=str)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', cast=str)
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', cast=str)
