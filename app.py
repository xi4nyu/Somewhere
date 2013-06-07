# coding: utf-8
#
# App run
#

import webapp2

from view.index import MainHandler, ExecHandler
from settings import DEBUG


app = webapp2.WSGIApplication([
  ('/', MainHandler),
  ('/exec', ExecHandler)
], debug=DEBUG)
