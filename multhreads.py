#!/usr/bin/env python
#!-- coding:utf-8 --


import threading
from uploadFiles import uploadfile
from uploadFiles import GetFileList
'''同时上传多个文件'''

class ThreadUpload(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        self.res = apply(self.func,self.args)

    def getResult(self):
        return self.res

fileList = ['F:\\20170403\\80FE5AA8A1FA726714C26BD3AE061BFB\\73413925B9C6B1ECE2D27FB6D7131353\\81300506ECC115D22A47D16BC66AF0EC.dcm',
            'F:\\20170403\\894C19C94ADAFD53ED54A5129D9EC7F3\\ED8D49F6852F054BD42C4815E3B4251E\\5376A6231199772E2C185B1D3DD78AED.dcm',
            'F:\\20170403\\89A30E54BFD348260CAD1E686462CE1F\\AFB27C836ABE229ADDDA3D60147AE1E9\\C85AFCABE0FA4EE1B3B56CA9BFD43756.dcm'
            ] #文件目录列表
# fileList = GetFileList('F:\\files',[])

def main():
    threads = []
    nloops = range(len(fileList))

    for i in nloops:
        t = ThreadUpload(uploadfile,('/apply/uploadImg',fileList[i]))
        t.setName(u'线程%s'% i)
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        threads[i].join()

    print u'执行完毕!'

if __name__ == '__main__':
    main()
