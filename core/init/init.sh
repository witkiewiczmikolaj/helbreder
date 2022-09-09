#!/bin/bash

export $(xargs < ./env/credentials.txt) \
&& cd ./app \
&& python3 -m flask run --host=0.0.0.0
