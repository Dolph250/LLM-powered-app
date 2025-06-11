# run_desktop.py
import os
import threading
import webview
from django.core.management import call_command
import django

# Set Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
django.setup()

# Start Django server in a thread
def start_django():
    call_command('runserver', '127.0.0.1:8000', '--noreload')

if __name__ == '__main__':
    threading.Thread(target=start_django, daemon=True).start()
    
    # Open a native desktop window
    webview.create_window("My Django Desktop App", "http://127.0.0.1:8000")
    webview.start()
