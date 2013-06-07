# coding: utf-8
#
# App run
#

import logging
import webapp2

from core.util import get_handlers
from settings import DEBUG


settings = {"debug": DEBUG}
handlers = get_handlers()

app = webapp2.WSGIApplication(handlers, **settings)
