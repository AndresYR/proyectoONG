"""
Django settings for proyectoONG project.

Generated by 'django-admin startproject' using Django 4.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-_1=_^&8_f^q6-!-*yp@=djf^r9qwc2sd=4r37v4o7p%u^zgpn^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Login Conf
LOGIN_URL = 'blog/login'

LOGIN_REDIRECT_URL = '../'

# Application definition

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOCAL_APPS = [
    'blog'
]

THIRD_APPS = [
    'tinymce',
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'proyectoONG.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'proyectoONG.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Argentina/Cordoba'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(str(BASE_DIR)+'/blog/static/blog', 'media/')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
# STATICFILES_DIRS = (
#     os.path.join(os.path.dirname(BASE_DIR), 'static'),
# )

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

TINYMCE_DEFAULT_CONFIG = {
    'plugins': 'print preview importcss tinydrive searchreplace autolink autosave save directionality visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists  wordcount imagetools textpattern noneditable help charmap quickbars emoticons blockquote',
    'menubar': 'file edit view insert format tools table tc help',
    'toolbar': 'undo redo | bold italic underline strikethrough | fontselect fontsizeselect formatselect | alignleft aligncenter alignright alignjustify | outdent indent |  numlist bullist checklist | forecolor backcolor casechange permanentpen formatpainter removeformat | pagebreak | charmap emoticons | fullscreen  preview save print | insertfile image media pageembed template link anchor codesample | a11ycheck ltr rtl | showcomments addcomment',
    # 'autosave_ask_before_unload': True,
    # 'autosave_interval': '30s',
    # 'autosave_prefix': '{path}{query}-{id}-',
    # 'autosave_restore_when_empty': False,
    # 'autosave_retention': '2m',
    # 'image_advtab': True,
    # 'automatic_uploads': False,
    # 'importcss_append': True,
    # 'templates': [
    #     {
    #         'title': 'New Table',
    #         'description': 'creates a new table',
    #         'content': '<div class="mceTmpl"><table width="98%%"  border="0" cellspacing="0" cellpadding="0"><tr><th scope="col"> </th><th scope="col"> </th></tr><tr><td> </td><td> </td></tr></table></div>'
    #     },
    #     {'title': 'Starting my story', 'description': 'A cure for writers block', 'content': 'Once upon a time...'},
    #     {
    #         'title': 'New list with dates',
    #         'description': 'New List with dates',
    #         'content': '<div class="mceTmpl"><span class="cdate">cdate</span><br /><span class="mdate">mdate</span><h2>My List</h2><ul><li></li><li></li></ul></div>'
    #     }
    # ],
    # 'template_cdate_format': '[Date Created (CDATE): %m/%d/%Y : %H:%M:%S]',
    # 'template_mdate_format': '[Date Modified (MDATE): %m/%d/%Y : %H:%M:%S]',
    'height': 600,
    'image_caption': True,
    # 'quickbars_selection_toolbar': 'bold italic | fontselect fontsizeselect formatselect',
    'noneditable_noneditable_class': 'mceNonEditable',
    'toolbar_mode': 'sliding',
    'spellchecker_ignore_list': ['Ephox', 'Moxiecode'],
    'tinycomments_mode': 'embedded',
    'content_style': '.mymention{ color: gray; }',
    'contextmenu': 'link image in',
    'a11y_advanced_options': True,
    'mentions_selector': '.mymention',
    'mentions_item_type': 'profile',
    "language": "es_ES",  # To force a specific language instead of the Django current language.
}
