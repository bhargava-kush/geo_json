web: gunicorn config.wsgi:application
worker: celery worker --app=geo_json.taskapp --loglevel=info
