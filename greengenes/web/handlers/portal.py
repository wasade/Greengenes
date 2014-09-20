from tornado.web import authenticated

from greengenes.web.handlers.base import BaseHandler


class PortalHandler(BaseHandler):
    @authenticated
    def get(self):
        self.render("portal.html", user=self.current_user)
