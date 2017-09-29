#!/usr/bin/env python
#!-- coding:utf-8 --
import string
import random
import hashlib
import os



class RzkKeywords(object):
    ROBOT_LIBRARY_SCOPE = 'Global'

    def getNoncestr(self):
        '''随机生成24位长度随机字符串，
           包含数字、大小写字母，作为noncestr 参数
        '''
        sample_str = string.letters + string.digits
        randomstr = random.sample(sample_str, 24)
        noncestr = ''
        for x in randomstr:
            noncestr += x
        return noncestr

    def md5(self,password_str):
        '''输入一个字符串，进行md5 32位加密，返回小写密文'''
        m = hashlib.md5()
        m.update(password_str)
        md5_str = m.hexdigest()
        return md5_str

    def getsign(self,apptoken, noncestr, usertoken=''):
        '''计算header里面的sign标志
           apptoken=@apptoken&noncestr=@noncestr&usertoken=@userToken&appkey=@ appkey 串MD5加密后转成大写'''
        appkey = 'KMEHosp@2016#WEB_TEST'
        if usertoken == '':
            password = 'apptoken=%s&noncestr=%s&appkey=%s' % (apptoken, noncestr, appkey)
            sign = str(RzkKeywords().md5(password)).upper()
            return sign
        else:
            password = 'apptoken=%s&noncestr=%s&usertoken=%s&appkey=%s' % (apptoken, noncestr, usertoken, appkey)
            sign = str(RzkKeywords().md5(password)).upper()
            return sign

    def fileList(self,filepath):
        '''指定文件路径，返回读取文件的列表'''
        f = open(filepath,'r')
        return [element.rstrip('\n') for element in f]

    def getAllFiles(self,dir, fileList=[]):
        '''指定一个文件夹路径，递归遍历到所有的文件，返回这些文件的全路径为元素的列表'''
        newDir = dir
        if os.path.isfile(dir):
            fileList.append(dir.decode('gbk'))
        elif os.path.isdir(dir):
            for s in os.listdir(dir):
                # 如果需要忽略某些文件夹，使用以下代码
                # if s == "xxx":
                # continue
                newDir = os.path.join(dir, s)
                RzkKeywords().getAllFiles(newDir, fileList)
        return fileList





if __name__ == '__main__':
    # Apptoken = '4ac990c260f947dd8cb589b68fbd652e'
    # noncestr = '2015457vk7ZaqgcF8KNMp1'
    # appkey = 'KMEHosp@2016#WEB_TEST'
    # print RzkKeywords().getsign(Apptoken,noncestr,appkey)
    # li = RzkKeywords().fileList('F:\\prarms.txt')
    li = RzkKeywords().getAllFiles('F:\\20170403')
    print li



