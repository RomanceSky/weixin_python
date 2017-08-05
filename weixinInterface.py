 #!/usr/bin/env python 
 # -*- coding: utf-8 -*-
import hashlib
import web
import time 
import os
# z增加的代码
import reply
import receive

web.config.debug = True

class WeixinInterface:
 
    def __init__(self):
        self.app_root = os.path.dirname(__file__)
        self.templates_root = os.path.join(self.app_root, 'templates')
        self.render = web.template.render(self.templates_root)
 
    def GET(self):
        #获取输入参数
        data = web.input()
        signature=data.signature
        timestamp=data.timestamp
        nonce=data.nonce
        echostr = data.echostr
        #自己的token
        token="myseasite" #这里改写你在微信公众平台里输入的token
        #字典序排序
        list=[token,timestamp,nonce]
        list.sort()
        sha1=hashlib.sha1()
        map(sha1.update,list)
        hashcode=sha1.hexdigest()
        #sha1加密算法
 
        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr
    def POST(self):
        try:
            webData = web.data()
            print "Handle Post webdata is ", webData   #后台打日志
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                content = "test"
                replyMsg = reply.TextMsg(toUser, fromUser, content)
                return replyMsg.send()
            else:
                print "暂且不处理"
                return "success"
            '''
            str_xml = web.data() #获得post来的数据
            xml = etree.fromstring(str_xml)#进行XML解析
            content=xml.find("Content").text#获得用户所输入的内容
            msgType=xml.find("MsgType").text
            fromUser=xml.find("FromUserName").text
            toUser=xml.find("ToUserName").text
            # 1
            #recMsg = receive.parse_xml(webData)
            #if msgType == 'text':
            #   content = xml.find("Content").text
                
                 #if content == 'help': 
                #    return self.render.reply_text(fromUser, toUser, int(time.time()), "随便看看？（对不起我功能有限QAQ）")
           

                    #return self.render.reply_text(fromUser, toUser, int(time.time()), "哎呀出错了 输入个help看看如何正确的调戏我？")
            #if msgType == 'event':
               # if xml.find("Event").text == 'subscribe':#关注的时候的欢迎语
               #     return self.render.reply_text(fromUser, toUser, int(time.time()), u"谢谢你的关注，输入help看看如何正确的调戏我")
except Exception, Argment:
        #    return Argment

'''
        except Exception, Argment:
            return Argment
            
        if type(content).__name__ == "unicode":
            content = xml.find('Content').text
            content = content.encode('UTF-8')
            Nword = youdao(content)
        return self.render.reply_text(fromUser,toUser,int(time.time()),Nword)
        #  return self.render.reply_text(fromUser,toUser,int(time.time()),u"我现在还在开发中，还没有什么功能，您刚才说的是："+content)
    def youdao(word):
        qword = urllib2.quote(word)
        baseurl = r'http://fanyi.youdao.com/openapi.do?keyfrom=yourAppName&key=yourAppKey&type=data&doctype=json&version=1.1&q='
        url = baseurl+qword
        resp = urllib2.urlopen(url)
        fanyi = json.loads(resp.read())
	##根据json是否返回一个叫“basic”的key来判断是否翻译成功
        if 'basic' in fanyi.keys():
		##下面是你自已来组织格式
            trans = u'%s:\n%s\n%s\n网络释义：\n%s'%(fanyi['query'],''.join(fanyi['translation']),''.join(fanyi['basic']['explains']),''.join(fanyi['web'][0]['value']))
            return trans
        else:
            return u'对不起，您输入的单词%s无法翻译，请检查拼写'% word
'''
 