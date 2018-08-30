install-dependencies:
	virtualenv ./venv
	./venv/bin/pip install Django

init-project:
	./venv/bin/django-admin startproject trader

server:
	( \
		cd trader; \
		../venv/bin/python manage.py migrate; \
		../venv/bin/python manage.py runserver 127.0.0.1:8888 \
		)

