import os

from .common import *


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY")
# Site
# https://docs.djangoproject.com/en/2.0/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS += ("gunicorn",)
DEBUG=False

# https://developers.google.com/web/fundamentals/performance/optimizing-content-efficiency/http-caching#cache-control
# Response can be cached by browser and any intermediary caches (i.e. it is "public") for up to 1 day
# 86400 = (60 seconds x 60 minutes x 24 hours)
AWS_HEADERS = {
    "Cache-Control": "max-age=86400, s-maxage=86400, must-revalidate",
}
