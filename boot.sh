#!/bin/sh
gunicorn -b 0.0.0.0:8000 -k gevent -w 5 Flask_Base_Template:app