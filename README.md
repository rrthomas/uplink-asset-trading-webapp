# Uplink Asset Trading Web application

This is a Django application for managing tradeable Uplink assets.

## Requirements

* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) version 3.6 or higher

## Getting started

`./scripts/setup.sh`
`./scripts/run-server.sh`

Use the included utility script to create some accounts (when the uplink node is running):

`pipenv run python scripts/create-test-accounts.py | tee test-accounts.txt`

You need to capture the output so that you have the private keys and account addresses
for subsequent transactions.

Use the [Uplink block explorer](http://localhost:8000/accounts/), to view accounts and assets.

Once the development server and the uplink node are running, visit http://localhost:8888/accounts/
You should see the addresses of all the accounts you created
