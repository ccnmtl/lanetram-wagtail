# Django settings for lanretam project.
import os.path
from ccnmtlsettings.shared import common

project = 'lanretam'
base = os.path.dirname(__file__)

locals().update(common(project=project, base=base))

PROJECT_APPS = [
    'lanretam.main',
]

USE_TZ = True

MIDDLEWARE += [  # noqa
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

INSTALLED_APPS += [  # noqa
    'bootstrap4',
    'infranil',
    'django_extensions',

    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.contrib.styleguide',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.admin',
    'wagtail.core',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',

    'lanretam.main',
]

THUMBNAIL_SUBDIR = "thumbs"
LOGIN_REDIRECT_URL = "/"

WAGTAIL_SITE_NAME = 'Lanretam'

WIND_AFFIL_HANDLERS = ['lanretam.main.auth.WagtailEditorMapper',
                       'djangowind.auth.StaffMapper',
                       'djangowind.auth.SuperuserMapper']
