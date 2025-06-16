import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "WorkOra.settings")
django.setup()

User = get_user_model()

username = "admin"
email = "admin@example.com"
password = "admin123"

if not User.objects.filter(username=username).exists():
    print("✅ Creating superuser...")
    User.objects.create_superuser(username=username, email=email, password=password)
else:
    print("✅ Superuser already exists.")
