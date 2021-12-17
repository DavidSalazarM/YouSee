release: python manage.py migrate
web: gunicorn yousee.wsgi --timeout 120 --keep-alive 10 --log-level debug
