#!/bin/bash

export FLASK_APP=app.py
export LC_ALL=C.UTF-8
export LANG=C.UTF-8

if [ ! -f /conf/.bootstrapped_ssd ]
then
	mv /ssd/* /conf/
	echo 1 > /conf/.bootstrapped_ssd
fi

cd /conf/
while(true)
do
	flask run -h 0.0.0.0
	sleep 5
done
