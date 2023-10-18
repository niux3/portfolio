#!/bin/bash

pipenv shell && export FLASK_ENV=development && export FLASK_APP=app && flask run -p 8000

