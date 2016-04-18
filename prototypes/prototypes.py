import os
import sys

from django.conf import settings


BASE_DIR = os.path.dirname(__file__)

DEBUG = os.environ.get('DEBUG', 'on') == 'on'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')
SECRET_KEY = os.environ.get('SECRET_KEY', 
                'o%_(jt*w((r$baw$@4_o_7s64^4j8@b)j6x=&o5r=9hh-v14zs')


settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF='sitebuilder.urls',
    MIDDLEWARE_CLASSES=(),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
        'sitebuilder',
    ),
    STATIC_URL='/static/',
    SITE_PAGES_DIR=os.path.join(BASE_DIR, 'pages')
)


if __name__ == '__main__':
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
