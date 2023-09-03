from E_LEARNING.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-*tezh%5njx^tg*+7ru7hsk0gwp4e*52-=n99%qf*p)9*4!#qe+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = [
    'multi_captcha_admin',
    'django.contrib.humanize',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'robots',
    'blog',
    'website',
    'taggit',
    'django_summernote',
    'captcha',
    'auth_app',
]


# sites framework
SITE_ID = 1


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# STATIC_ROOT = BASE_DIR / 'static'
MEDIA_ROOT = BASE_DIR / 'media'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

CSRF_COOKIE_SECURE = True