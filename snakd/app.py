import tornado.platform.twisted
tornado.platform.twisted.install()
import tornado.web
import tornado.httpserver
import tornado.ioloop

from urls import url_patterns
from settings import settings

class Application(tornado.web.Application):
    """
    Instances of tornado.web.Application

    Calls tornado.web.Application parent class to make up a web application.
    Pass a list of tuple to handle the urls and the settings dict
    """
    def __init__(self):
        tornado.web.Application.__init__(self, url_patterns, **settings)

if __name__ == "__main__":
    application = Application()
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()