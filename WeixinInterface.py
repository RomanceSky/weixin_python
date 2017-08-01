#coding=utf-8  
  
import hashlib  
import web  
import time  
import os  
from lxml import etree  
  
#hashlib用于加密，md5，hash等  
#lxml用来解析xml文件  
  
class WeixinInterface(object):  
    #初始化  
    def __init__(self):  
        #拼接路径  
        self.app_root = os.path.dirname(__file__)  
        self.templates_root = os.path.join(self.app_root,'templates')  
        #渲染模版  
        self.render = web.template.render(self.templates_root)  
  
    #使用get方法,接收微信的get请求,看开发者文档的说明  
    #http://mp.weixin.qq.com/wiki/8/f9a0b8382e0b77d87b3bcc1ce6fbc104.html  
    def GET(self):  
        data = web.input()  
        signature = data.signature#微信加密签名  
        timestamp = data.timestamp#时间戳  
        nonce = data.nonce#随机数  
        echostr = data.echostr#随即字符串  
        token = 'zq90857'#自己设置的token  
  
        #将token、timestamp、nonce三个参数进行字典序排序  
        list = [token,timestamp,nonce]  
        list.sort()  
        #将三个参数字符串拼接成一个字符串进行sha1加密  
        sha1=hashlib.sha1()  
        map(sha1.update,list)  
        temStr = sha1.hexdigest()#加密  
        #判断  
        if temStr == signature:  
            return echostr  
