#!/bin/bash

date_time=$(date)

echo -e  "\nZettaknight API server started at ${date_time}!\n"
python /opt/clemson/zfs_scripts/zettaknight/zettaknight_api/zettaknight_api/manage.py runserver 0.0.0.0:8000

