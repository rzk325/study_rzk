#/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from test_mathfunc import TestMathFunc

if __name__ == '__main__':
    suite = unittest.TestSuite()
    tests = []
    #构建suite
    tests.append(TestMathFunc("test_add"))
    tests.append(TestMathFunc("test_minus"))
    tests.append(TestMathFunc("test_divide"))
    suite.addTests(tests)
    #运行suite
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
    #将结果输出到文件中
    # with open('report.txt','a') as f :
    #     runner = unittest.TextTestRunner(stream=f,verbosity=2)
    #     runner.run(suite)
    # f.close()


