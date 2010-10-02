#!/bin/sh
. ENV.lin64/bin/activate
export PYTHONPATH=/home/darvin/workspace/qtdjango/src/
ENV.lin64/bin/python manage.py runserver
