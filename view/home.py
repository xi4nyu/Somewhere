# coding: utf-8
#
# Home Handler
#

from core.util import url
from core.web import BaseHandler


@url(r"/")
class MainHandler(BaseHandler):
    def get(self):
        self.render("index.html")



@url(r"/exec")
class ExecHandler(BaseHandler):
    def get(self):
        # check X-AppEngine-Cron header true
        if self.request.headers.get("X-AppEngine-Cron") == "true":
            self.debug("success")
        else:
            self.debug("failed")
