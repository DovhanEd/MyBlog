"""
Налаштування Django для проекту mysite.

Створено 'django-admin startproject' using Django 4.0.3.

Для отримання додаткової інформації про цей файл дивіться
https://docs.djangoproject.com/en/4.0/topics/settings/

Повний список налаштувань та їх значень дивіться
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Створіть шляхи всередині проекту наступним чином: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Налаштування швидкого запуску розробки - unsuitable for production
# Дивіться https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# ПОПЕРЕДЖЕННЯ ПРО БЕЗПЕКУ: тримайте секретний ключ, який використовується у виробництві, в секреті!
SECRET_KEY = 'django-insecure-j_48v*nl&@1_kl&f*+%iad#(ed=c3uq$#n)%g*-+0r&zqip$-v'

# Попередження про безпеку: не запускайте з включеною налагодженням в робочому середовищі!
DEBUG = True

ALLOWED_HOSTS = []


# Визначення програми

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_blog',
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

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# База даних
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Перевірка пароля
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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


# Інтернаціоналізація
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статичні файли (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'static/'

# Тип поля первинного ключа за замовчуванням
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
