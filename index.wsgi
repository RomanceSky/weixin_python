#coding: UTF-8
import os, sys

import sae
import web

from weixinInterface import WeixinInterface

reload(sys)
sys.setdefaultencoding( "utf-8" )
urls = (
'/myseasite','WeixinInterface'
)

app_root = os.path.dirname(__file__)
templates_root = os.path.join(app_root, 'templates')
render = web.template.render(templates_root)

app = web.application(urls, globals()).wsgifunc()        
application = sae.create_wsgi_app(app)



