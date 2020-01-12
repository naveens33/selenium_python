import unittest
import HtmlTestRunner

class HtmlReportExample(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setUpClass execute. ")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass execute. ")

    def setUp(self):
        unittest.TestCase.setUp(self)
        print("setUp method execute. ")

    def tearDown(self):
        unittest.TestCase.tearDown(self)
        print("tearDown method execute. ")

    def test_function_one(self):
        print("test_function_one execute.")
        self.assertEqual(1, 2, "test_function_one.")

    def test_function_two(self):
        print("test_function_two execute.")
        self.assertNotEqual(1, 2, "test_function_two.")

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner('./reports/html_report'))
    #HtmlTestRunner.main()