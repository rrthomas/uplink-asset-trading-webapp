install-dependencies:
	virtualenv ./venv
	./venv/bin/pip install Django

init-project:
	./venv/bin/django-admin startproject trader

