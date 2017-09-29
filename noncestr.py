#!/usr/bin/env python
#!-- coding:utf-8 --


import random
import string
import hashlib


def noncestr():
    sample_str = string.letters + string.digits
    random_str = random.sample(sample_str, 24)
    noncestr = ''
    for x in random_str:
        noncestr += x
    return noncestr


def md5(password_str):
    '''md5 加密字符串'''
    m = hashlib.md5()
    m.update(password_str)
    sign = m.hexdigest()
    return sign

if __name__ == '__main__':
    print md5('adfdfsfasfas')