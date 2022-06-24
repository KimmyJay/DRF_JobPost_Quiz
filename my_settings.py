from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'sampletable',
#         'USER': 'root',
#         'PASSWORD': 'rootroot',
#         'HOST': '127.0.0.1',
#         'PORT': '3306',
#         'OPTIONS': {'charset': 'utf8mb4'},
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

SECRET = {
    'secret': 'django-insecure-(pk9#2q%s@55qa=m7a5a3b-lvmg5wrbf-p=fptt%a(_hw0-@b_',
}


# https://docs.djangoproject.com/en/1.11/topics/logging/
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
