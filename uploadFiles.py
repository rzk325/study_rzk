#!/usr/bin/env python
#!-- coding:utf-8 --

import os
import requests
import json
import time


def GetFileList(dir, fileList):
    '''遍历到所有的文件名称路径'''
    newDir = dir
    if os.path.isfile(dir):
        fileList.append(dir.decode('gbk'))
    elif os.path.isdir(dir):
        for s in os.listdir(dir):
            #如果需要忽略某些文件夹，使用以下代码
            #if s == "xxx":
                #continue
            newDir=os.path.join(dir,s)
            GetFileList(newDir, fileList)
    return fileList


def mkdirfiles(mdir):
    '''写一个参数文件，里面是要发送的文件名称'''
    filelist = GetFileList(mdir, [])
    f = open(r'prarms.txt','w+')
    for lines in filelist:
        f.writelines(lines+'\n')
    f.close()



# URL_8080 = 'http://10.2.29.216:8080/kmhc-image-report-web'
URL_8080 = 'http://ir.kmwlyy.com:8080/kmhc-image-report-web'


def login(uri):
    url = URL_8080 + uri
    header = {}
    payload = {'username':'kmtest','password':'123456'}

    s = requests.session()
    resp = s.post(url,data=payload)
    # resp = requests.post(url,data=payload)
    if resp.status_code == 200:
        print u'<<<<<登录请求成功>>>>>'
        data = resp.json()
        return data


def uploadfile(uri,filepath):
    url = URL_8080 + uri
    data = login('/login')
    Authorization = data['content']['authorizationToken']

    files = {'file': open(filepath, 'rb')}
    # files = {'file': ('401FF3E5D64272B7DC589C7908641BE6.dcm', open(filepath, 'rb'), 'dcm')}

    heards1 = {
               'Authorization':''
               }
    heards1['Authorization'] = Authorization #认证

    print u'开始上传'
    start = time.clock() # 开始时间
    print u'上传中！！！！'
    resp = requests.post(url,headers=heards1,files=files)

    if resp.status_code == 200:
        end = time.clock()
        print u'HTTP: %s ' % resp.status_code
        print resp.text
        print u'总共耗时:%s秒' % (end - start)
    else:
        end = time.clock()
        print u'HTTP: %s ' % resp.status_code
        print resp.text
        print u'总共耗时:%s秒' % (end - start)


if __name__ == '__main__':
    list1 = GetFileList('F:\\20170403',[])
    # for x in list1:
    #     print x
    uploadfile('/apply/uploadImg',list1[7])
    raw_input(u'输入任意字符关闭窗口。')









