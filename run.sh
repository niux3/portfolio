#!/bin/bash

if [ ! -d "venv" ]
then
    virtualenv --python python3 venv && . venv/bin/activate && pip install -r requirements.txt
fi
. venv/bin/activate && export FLASK_ENV=development && export FLASK_APP=app && flask run -p 8000