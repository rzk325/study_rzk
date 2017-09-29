# /usr/bin/python
# encoding:utf-8

import unittest
import mathfunc

class TestMathFunc(unittest.TestCase):

    @classmethod
    def setUp(self):
        print "do something before test.Prepare environment."

    @classmethod
    def tearDown(self):
        print "do something after test.Clean up."

    def test_add(self):
        '''case add(a,b)'''
        self.assertEqual(3,mathfunc.add(1,2),'不相等')
        self.assertNotEqual(3,mathfunc.add(2,3))

    def test_minus(self):
        """Test method minus(a, b)"""
        self.assertEqual(1, mathfunc.minus(3, 2))

    def test_multi(self):
        """Test method multi(a, b)"""
        self.assertEqual(6, mathfunc.multi(2, 3))

    def test_divide(self):
        """Test method divide(a, b)"""
        self.assertEqual(2, mathfunc.divide(6, 3))
        self.assertEqual(2.5, mathfunc.divide(5, 2))

if __name__ == '__main__':
    unittest.main()