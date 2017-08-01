# -*- coding: utf-8 -*-
# filename: main.py
def sign(data):  
    arr = [weChat['token'], data['timestamp'], data['nonce']]
    arr = sorted(arr)
    tempStr = ''.join(arr)
    data = tempStr.encode('UTF-8')
    return sha1(data).hexdigest()