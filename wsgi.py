#!/usr/bin/env python3

import sys
import chat
from os.path import abspath
from os.path import dirname

# 设置当前目录为工作目录
sys.path.insert(0, abspath(dirname(__file__)))

application = chat.app


"""
chat.conf
[program:chat]
command=/usr/local/bin/gunicorn wsgi -c gunicorn.config.py
directory=/var/www/chat
autostart=true
autorestart=true


gunicorn.config.py

bind = '0.0.0.0:2001'
pid = '/tmp/bbs.pid'
"""