# coding: utf-8
#
# Web ReqeustHandler
#

import logging
import os.path

from google.appengine.ext.webapp import RequestHandler, template

from util import NOW
from settings import TEMPLATE_PATH


class BaseHandler(RequestHandler):
    def render(self, f, **kwargs):
        directory = os.path.abspath(".")
        path = os.path.join(directory, os.path.join(TEMPLATE_PATH, f))
        self.response.out.write(template.render(path, kwargs))


    def debug(self, s):
        logging.debug("%s %s" % (s, NOW()))
