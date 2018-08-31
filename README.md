# Uplink Asset Trading Web application

This is a django application for managing tradeable Uplink assets

## Requirements

* [Docker](https://www.docker.com/)
* [Python](https://www.python.org/) version 3.6 or higher, with [virtualenv](https://virtualenv.pypa.io/en/stable/)

## Getting started

`oake install-dependencies`
`make server`

In a separate window

`make run-uplink-node`

To create some accounts, use the [Uplink block explorer](http://localhost:8000/accounts/)

Once the development server and the uplink node are running, visit http://127.0.0.1:8888/accounts/
You should see the addresses of all the accounts you created

