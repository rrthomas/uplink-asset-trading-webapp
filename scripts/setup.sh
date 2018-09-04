# Set up Python/Django environment

# No good workaround known for this problem, which may only affect systems
# with patched python, such as Debian derivatives.
if [ -f ~/.pydistutils.cfg ]; then
    echo "Error: please remove or rename ~/.pydistutils.cfg"
    exit 1
fi

# Install pipenv (run pip3, as that should work on all systems)
pip3 install pipenv

# Install dependencies
pipenv install django "git+https://github.com/adjoint-io/uplink-sdk-python#egg=uplink-sdk-python"


# The following commands install the outline of the Django project:
# pipenv run django-admin startproject trader
# pipenv run sh -c "cd trader && python manage.py startapp accounts"
