"""
Local settings for aids_jiance project.

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

from .base import *  # noqa

# DEBUG
# ------------------------------------------------------------------------------
DEBUG = env.bool('DJANGO_DEBUG', default=True)
TEMPLATES[0]['OPTIONS']['debug'] = DEBUG

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env('DJANGO_SECRET_KEY', default='zLw~b-fjtX}K-j:kDj-|(7TK/f3~vRxj`E#J{3<A)oYQ94Ghyc')

# Mail settings
# ------------------------------------------------------------------------------

EMAIL_PORT = 1025

EMAIL_HOST = 'localhost'
EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                    default='django.core.mail.backends.console.EmailBackend')


# CACHING
# ------------------------------------------------------------------------------
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': ''
    }
}

ALLOWED_HOSTS = ["*"]
# django-debug-toolbar
# ------------------------------------------------------------------------------
# MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware', ]
# INSTALLED_APPS += ['debug_toolbar', ]

# INTERNAL_IPS = ['127.0.0.1', '10.0.2.2', ]
#
#
# import socket
# import os
# # tricks to have debug toolbar when developing with docker
# if os.environ.get('USE_DOCKER') == 'yes':
#     ip = socket.gethostbyname(socket.gethostname())
#     INTERNAL_IPS += [ip[:-1] + '1']

# DEBUG_TOOLBAR_CONFIG = {
#     'DISABLE_PANELS': [
#         'debug_toolbar.panels.redirects.RedirectsPanel',
#     ],
#     'SHOW_TEMPLATE_CONTEXT': True,
# }

# django-extensions
# ------------------------------------------------------------------------------
INSTALLED_APPS += ['django_extensions', ]

# TESTING
# ------------------------------------------------------------------------------
TEST_RUNNER = 'django.test.runner.DiscoverRunner'

# Your local stuff: Below this line define 3rd party library settings
# ------------------------------------------------------------------------------
DEBUG_TOOLBAR_CONFIG = {  'JQUERY_URL' : r"https://cdn.bootcss.com/jquery/2.2.3/jquery.slim.min.js"}
