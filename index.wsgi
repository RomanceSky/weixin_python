#coding: UTF-8
import os, sys

import sae
import web

from weixinInterface import WeixinInterface
from django.http import HttpResponse
reload(sys)
sys.setdefaultencoding( "utf-8" )
urls = (
'/','WeixinInterface'
)
 
app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)
# 1
HttpResponse.content_type = 'content-type:text'


#

def application(environ, start_response):
    start_response('200 ok', [('content-type', 'text/plain')])
    return ['Hello, SAE!']