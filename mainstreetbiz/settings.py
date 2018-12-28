"""
Django settings for mainstreetbiz project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
from decouple import config, Csv
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())


# Application definition

INSTALLED_APPS = [
    'buyersregistry.apps.BuyersregistryConfig',
    'endorsement.apps.EndorsementConfig',
    'news.apps.NewsConfig',
    'setting.apps.SettingConfig',
    'downloads.apps.DownloadsConfig',
    'blog.apps.BlogConfig',
    'contact.apps.ContactConfig',
    'realtor.apps.RealtorConfig',
    'listing.apps.ListingConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'ckeditor',
    'ckeditor_uploader',
    'import_export',
    'admin_reorder',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'admin_reorder.middleware.ModelAdminReorder',
]

ROOT_URLCONF = 'mainstreetbiz.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            # 'loaders': [
            #     # insert your TEMPLATE_LOADERS here
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
        },
    },
]

WSGI_APPLICATION = 'mainstreetbiz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'PORT': '5432',
        'HOST': 'localhost',
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

EMAIL_BACKEND = config(
    'EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('EMAIL_USE_TLS', default=True, cast=bool)

DEFAULT_FROM_EMAIL = 'Django Maharudra <noreply@maharudra.me>'
EMAIL_SUBJECT_PREFIX = '[Django Maharudra] '

# CK Editor settings
CKEDITOR_BASEPATH = "/static/ckeditor/ckeditor/"
CKEDITOR_UPLOAD_PATH = "images/"
FILE_UPLOAD_PERMISSIONS = 0o644
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755
CKEDITOR_CONFIGS = {
    'default': {
        # 'skin': 'moono',
        'skin': 'office2013',
        'toolbar_Basic': [
            ['Source', '-', 'Bold', 'Italic']
        ],
        'toolbar_YourCustomToolbarConfig': [
            # {'name': 'document', 'items': ['Source', '-', 'Save', 'NewPage', 'Preview', 'Print', '-', 'Templates']},
            {'name': 'clipboard', 'items': [
                'Cut', 'Copy', 'Paste', 'PasteText', 'PasteFromWord', '-', 'Undo', 'Redo']},
            {'name': 'editing', 'items': [
                'Find', 'Replace', '-', 'SelectAll']},
            # {'name': 'forms',
            #  'items': ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea', 'Select', 'Button', 'ImageButton',
            #    'HiddenField']},
            '/',
            {'name': 'basicstyles',
             'items': ['Bold', 'Italic', 'Underline', 'Strike', 'Subscript', 'Superscript', '-', 'RemoveFormat']},
            {'name': 'paragraph',
             'items': ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', '-', 'Blockquote', 'CreateDiv', '-',
                       'JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock', '-', 'BidiLtr', 'BidiRtl',
                       'Language']},
            {'name': 'links', 'items': ['Link', 'Unlink', 'Anchor']},
            {'name': 'insert',
             'items': ['Image', 'Youtube', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak', 'Iframe']},
            '/',
            {'name': 'styles', 'items': [
                'Styles', 'Format', 'Font', 'FontSize']},
            {'name': 'colors', 'items': ['TextColor', 'BGColor']},
            {'name': 'tools', 'items': ['ShowBlocks']},
            {'name': 'about', 'items': ['About']},
            '/',  # put this to force next toolbar on new line
            {'name': 'yourcustomtools', 'items': [
                # put the name of your editor.ui.addButton here
                'Preview',
                'Maximize',

            ]},
        ],
        'toolbar': 'YourCustomToolbarConfig',  # put selected toolbar config here
        # 'toolbarGroups': [{ 'name': 'document', 'groups': [ 'mode', 'document', 'doctools' ] }],
        # 'height': 291,
        'width': '100%',
        # 'filebrowserWindowHeight': 725,
        # 'filebrowserWindowWidth': 940,
        # 'toolbarCanCollapse': True,
        # 'mathJaxLib': '//cdn.mathjax.org/mathjax/2.2-latest/MathJax.js?config=TeX-AMS_HTML',
        'tabSpaces': 4,
        'extraPlugins': ','.join([
            'uploadimage',  # the upload image feature
            # your extra plugins here
            'div',
            'autolink',
            'autoembed',
            'embedsemantic',
            'autogrow',
            # 'devtools',
            'widget',
            'lineutils',
            'clipboard',
            'dialog',
            'dialogui',
            'elementspath',
            'embedbase',
            'embed',
            'basicstyles',
            'ckawesome',
            'pbckcode',
            'lightbox',
            'slideshow',
            'youtube',
        ]),
    }
}

# django messages
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}
# django-import-export start
IMPORT_EXPORT_USE_TRANSACTIONS = True
# django-import expport end

# django reorder apps start
ADMIN_REORDER = (
    # Keep original label and models
    'sites',

    # # Rename app
    # {'app': 'auth', 'label': 'Authorisation'},

    # # Reorder app models
    # {'app': 'auth', 'models': ('auth.User', 'auth.Group')},

    # # Exclude models
    # {'app': 'auth', 'models': ('auth.User', )},

    # # Cross-linked models
    # {'app': 'auth', 'models': ('auth.User', 'sites.Site')},

    # # models with custom name
    # {'app': 'auth', 'models': (
    #     'auth.Group',
    #     {'model': 'auth.User', 'label': 'Staff'},
    # )},
    {'app': 'auth', 'models': (
        'auth.User',
    )},
    {'app': 'setting', 'label': 'Site settings', 'models': (
        {'model': 'setting.SocialLink', 'label': 'Social links'},
        {'model': 'setting.Contact', 'label': 'Footer contact field'},
        {'model': 'setting.Home', 'label': 'Home Page '},
        {'model': 'setting.About', 'label': 'About Page '},
        {'model': 'setting.BuyingProcess', 'label': 'Buying Process Page '},
        {'model': 'setting.SellingProcess', 'label': 'Selling Process Page '},
        {'model': 'setting.BusinessFinance',
            'label': 'Business finance Page '},
    )},
    {'app': 'realtor', 'label': 'Realtors', 'models': (
        {'model': 'realtor.Realtor', 'label': 'Realtors'},
        {'model': 'realtor.Disclaimer', 'label': 'NDA & Disclaimer'},
        {'model': 'realtor.LegalDisclaimer', 'label': 'Legal Disclaimer Page'},
        {'model': 'realtor.PrivacyPolicy', 'label': 'Privacy Policy Page'},
    )},
    {'app': 'listing', 'label': 'Listing', 'models': (
        {'model': 'listing.Listing', 'label': 'Listings'},
        {'model': 'listing.FeaturedListing', 'label': 'Featured Listing'},
        {'model': 'listing.Business_Type', 'label': 'Business Types'},
        {'model': 'listing.Area', 'label': 'Area'},
        {'model': 'listing.Status', 'label': 'Status'},
    )},
    {'app': 'buyersregistry', 'label': 'Buyer\'s Registry', 'models': (
        {'model': 'buyersregistry.Register', 'label': 'Register'},
        {'model': 'buyersregistry.BuyersInventoryPage',
            'label': 'Buyer\'s Inventry Page'},
    )},
    {'app': 'blog', 'label': 'Blog', 'models': (
        {'model': 'blog.Article', 'label': 'Articles'},
    )},
    {'app': 'news', 'label': 'News', 'models': (
        {'model': 'news.News', 'label': 'News'},
    )},
    {'app': 'endorsement', 'label': 'Endorsements', 'models': (
        {'model': 'endorsement.Clients', 'label': 'Client Reviews'},
    )},
    {'app': 'contact', 'label': 'Contact', 'models': (
        {'model': 'contact.Contact', 'label': 'Contact Page'},
        {'model': 'contact.ContactSelling',
            'label': 'Contacts (Selling Page)'},
        {'model': 'contact.ContactModel', 'label': 'Contacts (Listing Page)'},
    )},
    {'app': 'downloads', 'label': 'Available Downloads', 'models': (
        {'model': 'downloads.Document', 'label': 'Documents'},
    )},

)

# django reorder apps end
