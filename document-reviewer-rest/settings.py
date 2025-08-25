from decouple import config

#External urls
REDIS_HOST = config("REDIS_HOST", default="redis-13251.crce182.ap-south-1-1.ec2.redns.redis-cloud.com")
REDIS_PORT = config("REDIS_PORT", default=13251)
REDIS_DB = config("REDIS_DB", default=0, cast=int)
REDIS_USERNAME = config("REDIS_USERNAME", default="default")
REDIS_PASSWORD = config("REDIS_PASSWORD", default='Pr790xdcjtj1HWdIvygcnDvZGtBwWzxd')
REQUEST_CHANNEL = config("REQUEST_CHANNEL", default="my_requests_channel")
MONGO_HOST = config('MONGO_HOST', default='lmongodb+srv://swamishweta:Shweta%40123@cluster0.pg6qthn.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
MONGO_PORT = config('MONGO_PORT', default= 27017)
  

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cfevsn8xt@mypra&t_68)vc$5aw$v)&$e1hp%@vr0#!89dn4q-'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'document_reviewer_rest_app',
    'drf_yasg',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'document-reviewer-rest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'document-reviewer-rest.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': 'mongodb',
        'CLIENT': {
            'host': config('MONGO_URI'),
        }
    }
}

REDIS_CONNECTION_PARAMS = {
    'host': REDIS_HOST,
    'port': int(REDIS_PORT),
    'db': REDIS_DB,
    'username': REDIS_USERNAME,
    'password': REDIS_PASSWORD,
    'ssl': True  # Redis Cloud requires SSL
}

# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'