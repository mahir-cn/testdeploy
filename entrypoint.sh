#!/usr/bin/env bash
./neo4j-community-3.5.5/bin/neo4j start
sleep 1m
python3 proj/manage.py install_labels
python3 proj/manage.py runserver 0.0.0.0:8000

