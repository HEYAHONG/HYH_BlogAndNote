#!/usr/bin/env python3
# 企业微信自建APP发送消息。
# 时间:2020-12-01

import requests
import sys
import os
import json

class WxWorkAPPError(RuntimeError):
    def __init__(self, arg):
        self.args = arg


class WxWorkAPP:
    # 企业ID
    corpid = ''

    # 自建APP密钥
    appsecret = ''

    # 自建APP的agentid
    agentid = 1000002

    def __init__(self):
        pass

    # 设置发送信息所需要的信息,如企业ID(_corpid),自建APP密钥(_appsecret)，自建APP的agentid(_agentid)
    @classmethod
    def setsetting(self, _corpid, _appsecret, _agentid):
        self.corpid = _corpid
        self.appsecret = _appsecret
        self.agentid = _agentid

    # 发送消息，要发送的人员(ToUser),要发送的部门(ToParty),发送的消息(Message)。其中要发送的人员与要发送的部门必须有一个有效，消息不能为空。
    @classmethod
    def sendmessage(self, ToUser, ToParty, Message):
        # 获取accesstoken
        token_url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=' + self.corpid + '&corpsecret=' + self.appsecret
        req = requests.get(token_url)
        if(req.status_code != 200):
            raise  WxWorkAPPError("WxWorkAPP Request AccessToken Error")

        accesstoken_json=req.json();
        accesstoken=''
        if('access_token' in accesstoken_json):
            accesstoken = req.json()['access_token']
        else:
            raise WxWorkAPPError("wxWorkAPP Get AccessToken Error")

        # 发送消息
        msgsend_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + accesstoken + '&debug=1'
        params = {
            "touser": ToUser,
            "toparty": ToParty,
            "msgtype": "text",
            "agentid": self.agentid,
            "text": {
                "content": Message
            },
            "safe": 0
        }
        req = requests.post(msgsend_url, data=json.dumps(params))
        if(req.status_code != 200):
            raise WxWorkAPPError("WxWorkAPP Request SendMessage Error")
        ret = json.loads(req.text)
        if(ret['errcode'] != 0):
            raise WxWorkAPPError('WxWorkAPP SendMessage Error：'+req.text)
