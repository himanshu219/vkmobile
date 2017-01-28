import os
import sys
import imp

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))

sys.path.append(PROJECT_PATH)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vkmobile.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
