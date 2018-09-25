import unittest
import sys
#from selenium import webdriver

class TestCase1(unittest.TestCase):
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