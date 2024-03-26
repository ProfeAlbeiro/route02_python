"""
WSGI config for dj45_practical_crud_contacts_parttwo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj45_practical_crud_contacts_parttwo.settings')

application = get_wsgi_application()