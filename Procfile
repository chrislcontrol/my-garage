migrate: python manage.py migrate
collectstatic: python manage.py collectstatic --noinput
web: gunicorn --reload --config gunicorn_config.py nix_proxy.wsgi --chdir /app -b 0.0.0.0:$GUNICORN_PORT
