#!/usr/bin/env python3

from aliyunsms.aliyunsms import aliyunsmserror
from aliyunsms.aliyunsms import aliyunsms

# 初始化sms对象(必须传入正确AccessKey及密钥)
sms=aliyunsms("","");

# 设置发送设置(必须传入正确的签名及模板代码)
sms.setsetting("",'')

# 发送短信
# 根据模板不同构造json对象（必须传入模板所需对象）
msg={
    "Name":"",
    "SystemName":"",
    "Time":"2020-12-01",
    "ErrorCode":"E_TEST",
    "EventContent":"测试"
}
# 调用发送函数(必须传入正确的电话号码及json对象)
ret=sms.sendsms("",msg)
# 打印结果
print(str(ret, encoding='utf-8'))

