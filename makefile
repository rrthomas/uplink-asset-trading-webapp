install-dependencies:
	virtualenv ./venv
	./venv/bin/pip install Django
	./venv/bin/pip install git+https://github.com/adjoint-io/uplink-sdk-python

init-project:
	./venv/bin/django-admin startproject trader
	cd trader
	../venv/bin/python manage.py startapp accounts

server:
	( \
		cd trader; \
		../venv/bin/python manage.py migrate; \
		../venv/bin/python manage.py runserver 127.0.0.1:8888 \
		)

