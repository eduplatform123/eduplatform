#!/usr/bin/env python
"""
Setup script for the educational platform
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

def main():
    """Setup the Django project"""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')
    
    try:
        django.setup()
    except Exception as e:
        print(f"Error setting up Django: {e}")
        return
    
    print("Setting up the educational platform...")
    
    # Make migrations
    print("Creating migrations...")
    try:
        execute_from_command_line(['manage.py', 'makemigrations'])
        print("✓ Migrations created successfully")
    except Exception as e:
        print(f"✗ Error creating migrations: {e}")
        return
    
    # Migrate
    print("Applying migrations...")
    try:
        execute_from_command_line(['manage.py', 'migrate'])
        print("✓ Migrations applied successfully")
    except Exception as e:
        print(f"✗ Error applying migrations: {e}")
        return
    
    # Create superuser
    print("Creating superuser...")
    try:
        execute_from_command_line(['manage.py', 'createsuperuser', '--noinput'])
        print("✓ Superuser created successfully")
    except Exception as e:
        print(f"✗ Error creating superuser: {e}")
        print("You can create a superuser manually with: python manage.py createsuperuser")
    
    print("\nSetup completed!")
    print("You can now run the server with: python manage.py runserver")

if __name__ == '__main__':
    main()
