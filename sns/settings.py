import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = 'oh@@!2i!wruo^paa9c27je4y(n$$7*$3f2=_uk(jst8rsgtc(5'

DEBUG = False

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'assy.apps.AssyConfig',#testapp
    'django.contrib.sites', #for djnago-allauth
    'allauth', #for djnago-allauth
    'allauth.account', #for djnago-allauth
    'allauth.socialaccount',#for djnago-allauth
    'channels',
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

ROOT_URLCONF = 'sns.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'templates', 'allauth'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media', 
            ],
        },
    },
]

WSGI_APPLICATION = 'sns.wsgi.application'
ASGI_APPLICATION = 'sns.routing.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'df21clh7nicae8',
        'USER': 'cpyrsoqlxhrmnz',
        'PASSWORD': 'c9e1e397ff3fd21caefc59e364ef70487c21559183af0cbce350df00e3d603ff',
        'HOST': 'ec2-18-235-109-97.compute-1.amazonaws.com',
        'POST': '5432',
    }
}



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

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

IMAGE_ROOT = os.path.join(BASE_DIR, 'images')#画像アップローダ
IMAGE_URL = '/images/'

#追加
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 認証方式を「メールアドレスとパスワード」に変更
ACCOUNT_AUTHENTICATION_METHOD = 'email'
# ユーザー名を使用する
ACCOUNT_USERNAME_REQUIRED = True

# ユーザー登録確認メールは送信しない
ACCOUNT_EMAIL_VERIFICATION = 'none'
# メールアドレスを必須項目にする
ACCOUNT_EMAIL_REQUIRED = True

#ユーザーモデルの拡張(customuser)
AUTH_USER_MODEL = 'assy.CustomUser'

SITE_ID = 1 #django-allauthがsitesフレームワークを使っているため

LOGIN_REDIRECT_URL = 'home'
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/login/'
ACCOUNT_LOGOUT_ON_GET = True

#signupformを指定
ACCOUNT_FORMS = {
    'signup' : 'assy.forms.CustomSignupForm',
}
#signupformからの情報をcustomusermodelに保存するのに必要
ACCOUNT_ADAPTER = 'assy.adapter.AccountAdapter'

try:
    from .local_settings import *
except ImportError:
    pass

if not DEBUG:
    SECRET_KEY = os.environ['SECRET_KEY']
    django_heroku.settings(locals())

import django_heroku #追加
    
ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #追加
]

db_from_env = dj_database_url.config(conn_max_age=600, ssl_require=True)
DATABASES['default'].update(db_from_env)