import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "surmantra.settings")

django.setup()

# Auto-run migrations and create superuser if none exist
from django.contrib.auth import get_user_model
from django.db import OperationalError
from django.core.management import call_command

try:
    call_command('migrate')
    User = get_user_model()
    if not User.objects.filter(username="admin").exists():
        User.objects.create_superuser("admin", "admin@example.com", "adminpassword")
        print("Superuser created: admin / adminpassword")
except OperationalError as e:
    print(f"DB error: {e}")

application = get_wsgi_application()
