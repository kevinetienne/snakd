from handlers.static import HomeHandler

#: a list of tuples containing a regex and an Handler
url_patterns = [
    (r"/", HomeHandler),
]