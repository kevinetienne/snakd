import os

DEBUG = False

PROJECT_ROOT = os.path.dirname(__file__)

#: None to load template relative to the calling file
TEMPLATE_DIR = os.path.join(PROJECT_ROOT, "templates")

#: our static folder where we are storing js, css, images...
STATIC_DIR = os.path.join(PROJECT_ROOT, "statics")

#: It defines the _xsrf input value, which we check on all POST requests to
#: prevent cross-site request forgery. If you have set the 'xsrf_cookies'
#: application setting, you must include this HTML within all of your HTML forms.
XSRF_COOKIES = True

#: It should be a long, random sequence of bytes to be used as the HMAC secret
#: for the signature.
COOKIE_SECRET = ""

#: url where an user is redirected to login
LOGIN_URL = "/auth/login"

settings = dict(
    template_path = TEMPLATE_DIR,
    static_path = STATIC_DIR,
    xsrf_cookies = XSRF_COOKIES,
    cookie_secret = COOKIE_SECRET,
    login_url = LOGIN_URL,
    debug = DEBUG
)

try:
    from local_settings import *
except ImportError:
    pass
