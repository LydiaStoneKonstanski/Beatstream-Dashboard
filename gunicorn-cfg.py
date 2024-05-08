# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us

Gunicorn is a pre-fork worker model HTTP server for running Python web applications.
It's commonly used to deploy web applications written in Python, such as Django or Flask,
and helps manage multiple concurrent requests efficiently.
"""

'''ip address set for local host'''
bind = '0.0.0.0:5005'

'''multiprocessing cpu count'''
workers = 1

'''LSK changed this. Formerly was accesslog = '_'''
accesslog = '/Beatstream-Dashboard/log/httpd2/access_log'
loglevel = 'debug'
capture_output = True
enable_stdio_inheritance = True
