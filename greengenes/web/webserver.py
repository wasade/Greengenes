from os.path import dirname, join
from base64 import b64encode
from uuid import uuid4

from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from tornado.web import Application, StaticFileHandler
from tornado.options import define, options, parse_command_line

from greengenes.web import config
from greengenes.web.handlers.base import MainHandler, NoPageHandler
from greengenes.web.handlers.auth import AuthLoginHandler, AuthLogoutHandler
from greengenes.web.handlers.portal import PortalHandler
from greengenes.web.handlers.query import (QueryHandler, OTUHandler,
                                           OTUSummaryHandler)
from greengenes.web.handlers.validate import (ValidateHandler,
                                              ValidateResultsHandler)
from greengenes.web.handlers.websocket import MessageHandler, WaitingRedirect


define("port", default=config.http_port, type=int)


DIRNAME = dirname(__file__)
STATIC_PATH = join(DIRNAME, "static")
TEMPLATE_PATH = join(DIRNAME, "templates")  # base folder for webpages
COOKIE_SECRET = b64encode(uuid4().bytes + uuid4().bytes)


class WebApplication(Application):
    def __init__(self):
        handlers = [
            (r"/", MainHandler),
            (r"/static/(.*)", StaticFileHandler,
             {"path": STATIC_PATH}),
            (r"/auth/login/", AuthLoginHandler),
            (r"/auth/logout/", AuthLogoutHandler),
            (r"/portal/", PortalHandler),
            (r"/query/", QueryHandler),
            (r"/query/([0-9]*)", QueryHandler),
            (r"/otu/([0-9]*)", OTUHandler),
            (r"/otu_summary/([0-9]*)", OTUSummaryHandler),
            (r"/validate/", ValidateHandler),
            (r"/validate_results", ValidateResultsHandler),
            (r"/waiting_redirect/(.*)", WaitingRedirect),
            (r"/consumer/", MessageHandler),
            (r".*", NoPageHandler)
        ]
        settings = {
            "template_path": TEMPLATE_PATH,
            "debug": config.debug,
            "cookie_secret": COOKIE_SECRET,
            "login_url": "/login/",
        }
        super(WebApplication, self).__init__(handlers, **settings)


def main():
    parse_command_line()
    http_server = HTTPServer(WebApplication())
    http_server.listen(options.port)
    IOLoop.instance().start()


if __name__ == "__main__":
    main()
