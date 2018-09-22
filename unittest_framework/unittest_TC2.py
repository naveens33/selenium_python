import unittest
#from selenium import webdriver

class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print("setUpClass")

    def setUp(self):
        print("setUP")

    def test_method3(self):
        print("test method3")

    def tearDown(self):
        print("tearDown")

    @classmethod
    def tearDownClass(inst):
        print("tearDownClass")

if __name__ == '__main__':
    unittest.main()