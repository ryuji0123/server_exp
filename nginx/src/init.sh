#!/bin/sh
nginx
nohup python3 /src/backend.py -p 81 &
nohup python3 /src/backend.py -p 82 &
/bin/bash