# Uplink Asset Trading Web application

This is a Django application for managing tradeable Uplink assets.

## Requirements

* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) version 3.6 or higher

## Getting started

`./scripts/setup.sh`

This sets up a Python environment with `pipenv` (which it also installs as
needed). You can run commands in this environment either by prefixing them
with `pipenv run`, or by starting a sub-shell with `pipenv shell` and then
running commands in the sub-shell. For brevity, the rest of this
documentation assumes that you have taken the latter option.

`./scripts/run-server.sh`

Once the development server and the uplink node are running, start up the
[webapp](http://localhost:8888/accounts). This will list the addresses of
any accounts you create.

You can use the [Uplink block explorer](http://localhost:8000/accounts/) for
a “behind-the-scenes” look.

To avoid needing to prefix commands with `pipenv run`, you can start a
sub-shell with `pipenv shell`.

## Create accounts

Use the included utility script to create some accounts (when the uplink
node is running):

`pipenv run python scripts/create-test-accounts.py | tee test-accounts.txt`

You need to capture the output so that you have the private keys and account
addresses for subsequent transactions.

## Create assets

The utility script `scripts/create-test-asset.py` can be used to create an
asset so that tokens can be transferred between accounts. The script needs
an account address and a private key:

```
./scripts/create-test-asset.py [address of issuing account] [private key of issuing account]

```

Use the [Uplink block explorer](http://localhost:8000/assets/) to view
assets.
