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
import sae
 
 
def app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    return ['Hello, world!']
 
 
application = sae.create_wsgi_app(app)