"""
WSGI config for backendoyh1 project.

It exposes the WSGI callable as a module-level variable named ``application``.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backendoyh1.settings')

# Create application FIRST
application = get_wsgi_application()

# Import Mongo initializer AFTER Django loads
try:
    from .mongo import init_mongo
    init_mongo()  # Run AFTER gunicorn fork – SAFE
except Exception as e:
    print("Mongo init failed:", e)
