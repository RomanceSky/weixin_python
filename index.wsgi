#coding=utf-8  
  
import os  
import sae  
import web  
  
from weixininterface import WeixinInterface  
  
#配置web的路由  
urls = (  
    '/weixin','WeixinInterface'  
)  
#拼接路径  
app_root=os.path.dirname(__file__)  
templates_root = os.path.join(app_root,'templates')  
#渲染模版  
render = web.template.render(templates_root)  
  
#启动app  
app = web.application(urls,globals()).wsgifunc()  
application = sae.create_wsgi_app(app)  