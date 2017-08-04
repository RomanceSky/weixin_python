#coding: UTF-8
import os

import sae
import web

from weixinInterface import WeixinInterface

urls = (
	'/weixin', 'WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)

'''
def application(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    
    interface = WeixinInterface()
    return interface.GET()
'''