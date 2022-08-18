command = '/root/.local/lib/python3.8/site-packages/gunicorn'
pythonpath = '/usr/bin/python3'
bind = '127.0.0.1:8000'
workers = 3
user = 'root'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=settings.settings'