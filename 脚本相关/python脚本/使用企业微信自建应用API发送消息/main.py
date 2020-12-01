#!/usr/bin/env python3
from WxWorkAPP.WxWorkAPP import WxWorkAPP
from WxWorkAPP.WxWorkAPP import WxWorkAPPError

wx = WxWorkAPP
#设置自建APP信息(需要替换成自己自建APP的相关信息)
wx.setsetting('ww4af7b847605f9e33','iVwvhUsUe1JKNKvFehU4lWzEg0qBkV9ur0ErEMKEgNI',1000002)
#发送消息
try:
    wx.sendmessage('', '2' , 'TestTTTTTT' );
except WxWorkAPPError as err:
    print(''.join(err.args))


