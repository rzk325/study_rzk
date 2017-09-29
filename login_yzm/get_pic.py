#!/usr/bin/env python
#!-*- coding:utf-8 -*-

import requests
import base64

codepicURL = 'http://www.pss-system.gov.cn/sipopublicsearch/portal/login-showPic.shtml'
valcode = requests.get(codepicURL)
print valcode.cookies['WEE_SID']


#将response的二进制内容写成图片文件，这是验证码图片
f = open('valcode.png','wb')
f.write(valcode.content)
f.close()

username = base64.b64encode('rzk325')
passwrod = base64.b64encode('k61621479')


code_pic = input('请输入验证码：')

data = {'j_loginsuccess_url':'',
        'j_validation_code':code_pic,
        'j_username':username,
        'j_password':passwrod
        }
data['j_validation_code'] = code_pic

print data

checkUrl = 'http://www.pss-system.gov.cn/sipopublicsearch/wee/platform/wee_security_check'
resp = requests.post(checkUrl, cookies = requests.utils.dict_from_cookiejar(valcode.cookies), data=data)

print resp.text