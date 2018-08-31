# Set up Python/Django environment

# Call venv with HOME set to empty string to avoid reading any
# ~/.pydistutils.cfg
HOME= python3 -m venv venv

# Enter the venv
source ./venv/bin/activate

# Install dependencies
pip --isolated install Django git+https://github.com/adjoint-io/uplink-sdk-python
