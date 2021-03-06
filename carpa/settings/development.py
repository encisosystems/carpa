from .common import *
import dj_database_url

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'p3gm=o9o+_r(5*o$$kn#h*8#n1r)aquf^^nm_v5u0pn^qa$=4*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['*']


def show_toolbar(request):
    """
    The default callback checks if the IP is internal, but docker's IP
    addresses are not in INTERNAL_IPS, so we force the display in dev mode
    :param request: The intercepted request
    :return: True
    """
    return True


# CORS Config: install django-cors-headers and uncomment the following to allow CORS from any origin
DEV_APPS = [
    'debug_toolbar',
    # 'corsheaders'
]

INSTALLED_APPS += DEV_APPS


DEV_MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    # 'corsheaders.middleware.CorsMiddleware'
]

MIDDLEWARE = MIDDLEWARE + DEV_MIDDLEWARE  # CORS middleware should be at the top of the list

# CORS_ORIGIN_ALLOW_ALL = True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
    'SKIP_TEMPLATE_PREFIXES': (
        'django/forms/widgets/',
        'admin/widgets/',
        'menus/',
        'pipeline/',
    ),
}

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

# Configured with DATABASE_URL env, usually from dokku
if os.environ.get('DATABASE_URL', ''):
    DATABASES = {
        'default': dj_database_url.config()
    }
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

# Database for CI/CD github actions
elif os.environ.get('GITHUB_WORKFLOW'):
    DATABASES = {
        'default': {
           'ENGINE': 'django.contrib.gis.db.backends.postgis',
           'NAME': 'postgres',
           'USER': 'postgres',
           'PASSWORD': 'postgres',
           'HOST': '127.0.0.1',
           'PORT': '5432',
        }
    }

else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'postgres',
            'HOST': 'db',
            'PORT': 5432,
        }
    }
