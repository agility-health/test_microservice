#!/usr/bin/env bash

nohup poetry run flask run --host 0.0.0.0 &
poetry run python worker.py
