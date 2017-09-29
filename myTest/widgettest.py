# /usr/bin/python
# encoding:utf-8


from Widget import Widget
import unittest


class WidgetTestCase(unittest.TestCase):
    # 对象的初始化工作可以在setUp()方法中完成
    def setUp(self):
        self.widget = Widget()

    # 对象的资源的释放则可以在tearDown()方法中完成
    def tearDown(self):
        self.widget = None

    # 对应widget类中的get_size函数测试
    def test_size(self):
        self.assertEqual(self.widget.get_size(),(40,40))

    # 对应widget类中resize函数的测试
    def test_Resize(self):
        self.widget.resize(100,100)
        self.assertEqual(self.widget.get_size(),(10,100),msg='不相等')

if __name__ == '__main__':
    # unittest.main()
    # 构造测试suite
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('test_size'))
    suite.addTest(WidgetTestCase('test_Resize'))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)

