from .base import *
import os

DEBUG = False

# In production, require SECRET_KEY and ALLOWED_HOSTS
SECRET_KEY = os.environ['DJANGO_SECRET_KEY']
ALLOWED_HOSTS = os.environ.get('DJANGO_ALLOWED_HOSTS', '').split(',')

# Example: configure database from DATABASE_URL or env vars (left minimal)
