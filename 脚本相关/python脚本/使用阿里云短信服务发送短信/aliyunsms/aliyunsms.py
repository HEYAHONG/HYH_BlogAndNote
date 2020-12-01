#!/usr/bin/env python3
# 阿里云短信服务发送消息。
# 需要先行使用pip install aliyun-python-sdk-core安装SDK
# 时间:2020-12-01
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

class aliyunsmserror(RuntimeError):
    def __init__(self, arg):
        self.args = arg
class aliyunsms:
    #用于发送短信的Key
    accesskey=""
    #用于发送短信的Key的密钥
    accesssecret=""
    #区域
    regionid='cn-hangzhou'
    # 签名名称
    SignName=''
    # 短信模板名称
    TemplateCode=''
    @classmethod
    def __init__(self,_accessKeyId,_accessSecret,_RegionId='cn-hangzhou'):
        self.accesskey=_accessKeyId
        self.accesssecret=_accessSecret
        self.regionid=_RegionId
    # 设置短信发送信息（短信签名及模板）
    @classmethod
    def setsetting(self,_SignName,_TemplateCode):
        self.SignName=_SignName
        self.TemplateCode=_TemplateCode
    # 发送短信（传入电话号码及模板中的值的json对象（非字符串））
    @classmethod
    def sendsms(self,PhoneNumber,Content):
        client = AcsClient(self.accesskey, self.accesssecret, self.regionid)
        request = CommonRequest()
        request.set_accept_format('json')
        request.set_domain('dysmsapi.aliyuncs.com')
        request.set_method('POST')
        request.set_protocol_type('https')  # https | http
        request.set_version('2017-05-25')
        request.set_action_name('SendSms')
        request.add_query_param('RegionId', self.regionid)
        request.add_query_param('PhoneNumbers', PhoneNumber)
        request.add_query_param('SignName', self.SignName)
        request.add_query_param('TemplateCode', self.TemplateCode)
        request.add_query_param('TemplateParam',json.dumps(Content) )
        response = client.do_action(request)
        # print(str(response, encoding='utf-8'))
        return response




