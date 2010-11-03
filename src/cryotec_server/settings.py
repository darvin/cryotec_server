# Django settings for cryotec_service project.

import os


DEBUG = True
DEBUG_TOOLBAR = False
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
__PATH_TO_SETTINGS = os.path.abspath(os.path.dirname(__file__))
MANAGERS = ADMINS

DATABASE_ENGINE = 'sqlite3'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = os.path.join(os.path.dirname(__file__), '..', '..', 'cryotek.db')
DATABASE_USER = ''             # Not used with sqlite3.
DATABASE_PASSWORD = ''         # Not used with sqlite3.
DATABASE_HOST = ''             # Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''             # Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), 'media')


# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/site_media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '%8^5t2ms&#2$dfy&%hbsmffshi01u=)rbm)h4p#s&3j*&*&7e#'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.load_template_source',
    'django.template.loaders.app_directories.load_template_source',
#     'django.template.loaders.eggs.load_template_source',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    "django.middleware.gzip.GZipMiddleware",
)

ROOT_URLCONF = 'cryotec_server.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates'),
)

INSTALLED_APPS = (
#    'admin_tools',
#    'admin_tools.theming',
#    'admin_tools.menu',
#    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.markup',
    'machines',
    'clients',
    'actions',
    'actiontemplates',
    'files',
    'checklists',
    'django_extensions',
    'qtdjango.django_qtdjango',
    'south',
    'libs',
)

#apps that has qtdjango api
QTDJANGO_APPS = (
    "machines",
    "actions",
    "actiontemplates",
    "clients",
    "checklists",
               )

ADMIN_TOOLS_INDEX_DASHBOARD = 'cryotec_server.dashboard.CustomIndexDashboard'



SERIALIZATION_MODULES = {
  #  'json': 'wadofstuff.django.serializers.json'
}

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",   
    )



if DEBUG_TOOLBAR:
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INSTALLED_APPS += ('debug_toolbar',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_PANELS = (
        #'debug_toolbar.panels.version.VersionDebugPanel',
        'debug_toolbar.panels.timer.TimerDebugPanel',
        'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
        'debug_toolbar.panels.headers.HeaderDebugPanel',
        'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
        'debug_toolbar.panels.template.TemplateDebugPanel',
        'debug_toolbar.panels.sql.SQLDebugPanel',
        'debug_toolbar.panels.cache.CacheDebugPanel',
        'debug_toolbar.panels.logger.LoggingPanel',
    )
    DEBUG_TOOLBAR_CONFIG = {
        'EXCLUDE_URLS': ('/admin',),
        'INTERCEPT_REDIRECTS': False,
    }


MY_SITE_PROTOCOL = "http"
MY_SITE_PORT = "8000"