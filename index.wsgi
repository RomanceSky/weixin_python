# -*- coding: utf-8 -*-
# filename: main.py
import web

urls = (
    '/wei', 'Handle',
)

class Handle(object):
    def GET(self):
        return "hello, this is a test"

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
    
application = sae.create_wsgi_app(app)