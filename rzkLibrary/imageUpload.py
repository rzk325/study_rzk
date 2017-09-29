#!usr/bin/env python
#! -- coding:utf-8 --

import requests
from rzkLibrary import myKeywords
import do_api_1

url_8027 = r'https://tstore.kmwlyy.com:8027'

def imageUpload(uri,apptoken,usertoken):
    URL = url_8027 + uri
    heards1 = {'content-type': 'multipart/form-data;',
               'apptoken': '',
               'usertoken': '',
               'noncestr': '',
               'sign': ''
               }

    noncestr = myKeywords.RzkKeywords().getNoncestr()
    sign = myKeywords.RzkKeywords().getsign(apptoken, noncestr,usertoken)


    heards1['apptoken'] = apptoken
    heards1['noncestr'] = noncestr
    heards1['sign'] = sign
    print heards1['sign']

    files = {'file':('logout.png',open('F:\\logout.png','rb'),'image/png')}
    print '开始上传'
    r = requests.post(URL,files=files,headers=heards1)
    print r.status_code
    print r.text


if __name__ == '__main__':

    apptoken = do_api_1.getApptoken('/Common/GetAppToken')
    resp = do_api_1.login('/users/Login', apptoken)
    jsonData = resp.json()
    usertoken = jsonData['Data']['UserToken']
    print apptoken,usertoken
    imageUpload('/Upload/Image',apptoken,usertoken)