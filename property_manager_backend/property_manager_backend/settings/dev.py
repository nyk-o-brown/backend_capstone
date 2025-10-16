from .base import *
import os
from dotenv import load_dotenv  # Correct import

DEBUG = True

# Allow localhost by default in dev
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# Optionally load additional local env vars from a .env file
try:
    load_dotenv(os.path.join(BASE_DIR, '.env'))
except Exception as e:
    print(f"Failed to load .env file: {e}")
