from tornado.testing import AsyncHTTPTestCase
from tornado.web import Application
from snakd import urls
from snakd import settings

class UrlTest(AsyncHTTPTestCase):
    def get_app(self):
        return Application(urls.url_patterns, **settings)

    def test_homepage(self):
        response = self.fetch('/')
        self.assertEqual(response.code, 200, "homepage should return 200")

