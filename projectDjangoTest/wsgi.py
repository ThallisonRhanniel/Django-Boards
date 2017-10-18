import os
from dj_static import Cling # dj-static
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectDjangoTest.settings")

application = Cling(get_wsgi_application())
