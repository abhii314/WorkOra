#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WorkOra.settings')
    
    try:
        from django.core.management import execute_from_command_line

        # ✅ Auto-create admin if needed
        if 'runserver' in sys.argv or 'gunicorn' in sys.argv:
            try:
                import create_superuser
            except Exception as e:
                print("⚠️ Superuser creation failed or already exists:", e)

        execute_from_command_line(sys.argv)

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

if __name__ == '__main__':
    main()
