install-dependencies:
	virtualenv ./venv
	./venv/bin/pip install Django
	./venv/bin/pip install git+https://github.com/adjoint-io/uplink-sdk-python

# Don't run this. It shouldn't be necessary. I'm just keeping it here so that
# the underlying steps are documented
init-project:
	./venv/bin/django-admin startproject trader
	cd trader
	../venv/bin/python manage.py startapp accounts

# Run this in a separate window
run-uplink-node:
	docker run -it -p 8000:8000 -p 8545:8545 --name uplink --rm uplinkdlt/uplink:latest

server:
	( \
		cd trader; \
		../venv/bin/python manage.py migrate; \
		../venv/bin/python manage.py runserver 127.0.0.1:8888 \
		)

