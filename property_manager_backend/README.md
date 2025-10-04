Property Manager Backend

This folder contains the Django project for the Property Manager backend.

Quick start (local):

1. Create a virtualenv and activate it.
2. pip install -r requirements.txt
3. Copy `.env` and set your DJANGO_SECRET_KEY if desired.
4. python manage.py migrate
5. python manage.py runserver

Project structure mirrors a common Django layout with a split `settings` package and `apps/` for local apps.
