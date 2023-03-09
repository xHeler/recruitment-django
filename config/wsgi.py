"""
WSGI config for src project.
It exposes the WSGI callable as a module-level variable named ``application``.
For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/gunicorn/
"""

from configurations.wsgi import get_wsgi_application  # noqa

application = get_wsgi_application()
