def wexin(request):
    """
    所有的消息都会先进入这个函数进行处理，函数包含两个功能，
    微信接入验证是GET方法，
    微信正常的收发消息是用POST方法。
    """
    # 这个WEIXIN_TOKEN是在测试号的配置页面中配置的，等会会讲到
    WEIXIN_TOKEN = 'tangzongyu'
    if request.method == "GET":
        signature = request.GET.get("signature", None)
        timestamp = request.GET.get("timestamp", None)
        nonce = request.GET.get("nonce", None)
        echostr = request.GET.get("echostr", None)
        token = WEIXIN_TOKEN
        tmp_list = [token, timestamp, nonce]
        tmp_list.sort()
        tmp_str = "%s%s%s" % tuple(tmp_list)
        tmp_str = hashlib.sha1(tmp_str).hexdigest()
        if tmp_str == signature:
            return HttpResponse(echostr)
        else:
            return HttpResponse("error")#此处省略上面的那一段GET请求代码
    else:
        xml = request.body
        msg = parse_message(xml)
        if msg.type == 'text':
            #获取文本内容
            content = msg.content
            try:
                reply = TextReply(content=content,message=msg)
                r_xml = reply.render()
                # 获取唯一标记用户的openid，下文介绍获取用户信息会用到
                openid = msg.source
                return HttpResponse(r_xml)
            except Exception as e:
                #自行处理
                pass
        