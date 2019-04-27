#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/FLASKAPPS/ld44/")

from ld44 import app as application
application.secret_key = '\xa5^\xf7\x02\xf8\x94\x8f\xacb\x8a7\x15\xc4\xe8#\xf9\xc8\x8f\xed/\x85@v\x80'
