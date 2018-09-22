import unittest
#from selenium import webdriver

class TestCase1(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print("setUpClass")

    def setUp(self):
        print("setUP")

    def test_method1(self):
        print("test method1")

    def test_method2(self):
        print("test method2")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(inst):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()