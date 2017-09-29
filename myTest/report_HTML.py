#/usr/bin/env python
#-*-coding:utf-8-*-

import unittest
from test_mathfunc import TestMathFunc
from HTMLTestRunner import HTMLTestRunner


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))

    with open('HTMLReport.html','w') as f:
        runner = HTMLTestRunner(stream=f,
                                title='MathFunc Test Report',
                                description='generated by HTMLTestRunner.',
                                verbosity=2
                                )
        runner.run(suite)