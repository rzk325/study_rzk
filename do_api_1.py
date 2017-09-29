#!/usr/bin/env python
#!-- coding:utf-8 --

import requests
import json
import time
import random
import string
import hashlib

from rzkLibrary import myKeywords

url_8015 = r'https://tapi.kmwlyy.com:8015'
url_8017 = r'https://twww.kmwlyy.com:8017'
url_8060 = r'https://tuser.kmwlyy.com:8060'
url_8027 = r'https://tstore.kmwlyy.com:8027'


def getApptoken(uri):
    '''获得apptonken接口'''
    URL = url_8017 + uri
    ts = time.time()
    time_str = str(ts).replace('.','1')
    parms = {}
    parms['_']= time_str
    resp = requests.get(URL,parms)
    respData = resp.json()
    apptoken = respData['Data']['Token']
    return apptoken


def login(uri,apptoken):
    '''登录接口'''
    url = url_8015 + uri
    # payload = {"Mobile":"18871008856","Password":"k61621479","VerifyCode":"","UserType":1}
    payload = {"Mobile": "18871159918", "Password": "k61621479", "VerifyCode": "", "UserType": 1}
    heards1 = { 'content-type': 'application/json;charset=utf-8',
                'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:22.0) Gecko/20100101 Firefox/22.0',
                'Referer': 'https: // twww.kmwlyy.com:8017 /',
                'apptoken':'',
                'usertoken':'',
                'noncestr':'',
                'sign':''
                }

    noncestr = myKeywords.RzkKeywords().getNoncestr()
    sign = myKeywords.RzkKeywords().getsign(apptoken,noncestr)

    heards1['apptoken'] = apptoken
    heards1['noncestr'] = noncestr
    heards1['sign'] = sign

    resp = requests.post(url,json.dumps(payload), headers=heards1)
    return resp


def set_headers():
    '''设置带登录的请求头'''
    apptoken = getApptoken('/Common/GetAppToken')
    resp = login('/users/Login', apptoken)
    temp = resp.json()
    usertoken = temp['Data']['UserToken']
    heards1 = {'content-type': 'multipart/form-data;',
               'apptoken': '',
               'usertoken': '',
               'noncestr': '',
               'sign': ''
               }
    noncestr = myKeywords.RzkKeywords().getNoncestr()
    sign = myKeywords.RzkKeywords().getsign(apptoken, noncestr, usertoken)
    heards1['apptoken'] = apptoken
    heards1['usertoken'] = usertoken
    heards1['noncestr'] = noncestr
    heards1['sign'] = sign
    return heards1


def getFeedback(uri):
    '''查看反馈详情接口'''
    url = url_8015 + uri
    heards1 = set_headers()
    payload = {'id':'e8071a6203ca4c04bea4c3e220c19f8e'}
    r = requests.get(url,params=payload,headers=heards1)
    print r.status_code
    print r.request.headers
    print r.text


def image(uri):
    '''图片文件上传接口'''
    url = url_8027 + uri
    heards1 = set_headers()
    heards1.pop('content-type') #此处注意，应该去掉 content-type，就算设置为multipart/form-data一样错误，服务器500。泪流满面

    files = {'file': ('logout.png', open('F:\\logout.png', 'rb'), 'image/png')}
    print '开始上传'
    r = requests.post(url, files=files, headers=heards1)
    print r.status_code
    print r.text


if __name__ == '__main__':
    # apptoken  = getApptoken('/Common/GetAppToken')
    # resp = login('/users/Login',apptoken)
    # temp = resp.json()
    # utoken = temp['Data']['UserToken']
    image('//Upload/Image')
    # getFeedback('/UserFeedbacks/GetFeedback')











