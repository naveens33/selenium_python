import unittest
import sys
import datetime
#from selenium import webdriver

class TestCase1(unittest.TestCase):
    obj = datetime.datetime.now()
    @classmethod
    def setUpClass(inst):
        print("setUpClass")

    def setUp(self):
        print("setUP")

    def test_method1(self):
        print("test method1")

    @unittest.skip("Skip Test")
    def test_method2(self):
        print("test method2")

    @unittest.skipUnless(sys.platform.startswith("linux"), "requires Linux")
    def test_method3(self):
        print("test method3")

    @unittest.skipIf(int(obj.strftime("%d"))<3,"Only after 5th you can execute this test")
    def test_04(self):
        print("test04")

    @unittest.expectedFailure
    def test_method4(self):
        self.assertEqual(33, 27, "not equal")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(inst):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()