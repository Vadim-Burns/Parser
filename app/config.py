"""
This file contains configuration variables
"""

import os

# Rabbit config
_RABBIT_HOST = os.environ.get('RABBIT_HOST', 'localhost')
_RABBIT_USER = os.environ.get('RABBIT_USER', 'guest')
_RABBIT_PASSWORD = os.environ.get('RABBIT_PASSWORD', 'guest')
_RABBIT_PORT = os.environ.get('RABBIT_PORT', 5672)
RABBIT_CONNECT_URL = f'amqp://{_RABBIT_USER}:{_RABBIT_PASSWORD}@{_RABBIT_HOST}:{_RABBIT_PORT}/%2F'
RABBIT_QUEUE = os.environ.get('RABBIT_QUEUE')
