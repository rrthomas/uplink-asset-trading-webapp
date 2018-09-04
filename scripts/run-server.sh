#!/usr/bin/env bash
# Run uplink and django

function cleanup() {
    docker kill $ID
}

ID=`docker run --detach -it -p 8000:8000 -p 8545:8545 --name uplink --rm uplinkdlt/uplink:latest`
trap cleanup SIGINT

cd trader
python manage.py migrate
python manage.py runserver localhost:8888
