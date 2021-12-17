  
release: python manage.py migrate
web: gunicorn yousee.wsgi --timeout 500 --keep-alive 100 --log-level debug