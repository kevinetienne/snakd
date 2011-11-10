import tornado.web

class HomeHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.render("home.html")