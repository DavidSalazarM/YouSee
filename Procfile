  
release: python manage.py migrate
web: gunicorn yousee.wsgi --timeout 150 --keep-alive 30 --log-level debug