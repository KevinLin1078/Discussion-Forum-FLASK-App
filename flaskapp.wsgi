#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.append('/usr/local/lib/python2.7/dist-packages/')
sys.path.append('/usr/local/lib/python2.7/site-packages/')
sys.path.insert(0,"/var/www/FlaskApp/")
import pymongo

from FlaskApp import app as application
application.secret_key = 'Add your secret key'
