# run_server.py
import sys
import os
from django.core.management import execute_from_command_line

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

if __name__ == '__main__':
    sys.argv = ['manage.py', 'runserver']
    execute_from_command_line(sys.argv)
