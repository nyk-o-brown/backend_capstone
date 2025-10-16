from .base import *
import os

DEBUG = True

# Allow localhost by default in dev
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Use sqlite by default in dev (already configured in base)

# Optionally load additional local env vars from a .env file
try:
    from dot
    env import load_dotenv
    load_dotenv(os.path.join(BASE_DIR, '.env'))
except Exception:
    pass
