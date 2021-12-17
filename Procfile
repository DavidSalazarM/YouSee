  
release: python manage.py migrate
web: gunicorn yousee.wsgi --timeout 30 --keep-alive 10 --log-level debug