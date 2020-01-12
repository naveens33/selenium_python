import unittest
import HtmlTestRunner
import xmlrunner

class MyTestExample(unittest.TestCase):
    '''
    This class demo how to setup test case and run test use python unittest module.
    '''

    # This method will be executed only once for this test case class.
    # It will execute before all test methods. Must decorated with @classmethod.
    @classmethod
    def setUpClass(cls):
        print("setUpClass execute. ")

    # Similar with setupClass method, it will be executed after all test method run.
    @classmethod
    def tearDownClass(cls):
        print("tearDownClass execute. ")

        # This method will be executed before each test function.

    def setUp(self):
        unittest.TestCase.setUp(self)
        print("setUp method execute. ")

    # This method will be executed after each test function.
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        print("tearDown method execute. ")

    def test_function_one(self):
        print("test_function_one execute.")
        self.assertEqual(1, 2, "test_function_one.")

    def test_function_two(self):
        print("test_function_two execute.")
        self.assertNotEqual(1, 2, "test_function_two.")


html_report_dir = './html_report'
xml_report_dir = './reports/xml_report'

'''
# Run all test functions.
def run_all_test():
    # Run all test functions.
    unittest.main()


# Run all test function and generate html report.
def run_all_test_generate_html_report():
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))


# Run all test function and generate html report.
def run_all_test_generate_xml_report():
    # Run all test functions with HtmlTestRunner to generate html test report.
    unittest.main(testRunner=xmlrunner.XMLTestRunner(output=xml_report_dir))


# Run specified test functions in test suite.
def run_test_suite(test_function_name):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Add test function in the suite.
    test_suite.addTest(HtmlReportExample(test_function_name))

    # Run test suite and get test result.
    testResult = unittest.TestResult()
    test_suite.run(testResult)
    print(testResult)


# Run specified test functions and generate html test report.
def run_test_suite_generate_html_report(test_function_name):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Add test function in the suite.
    test_suite.addTest(HtmlReportExample(test_function_name))

    # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)


# Run specified test functions and generate xml test report.
def run_test_suite_generate_xml_report(test_function_name):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()
    # Add test function in the suite.
    test_suite.addTest(HtmlReportExample(test_function_name))
    # Create HtmlTestRunner object and run the test suite.
    test_runner = xmlrunner.XMLTestRunner(output=xml_report_dir)
    test_runner.run(test_suite)


# Run all test functions in the specified test case class, the function parameter must be a class name not the class name string.
def run_all_test_in_class(test_case_class):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Make all test function
    test = unittest.makeSuite(test_case_class)
    test_suite.addTest(test)

    # Create a test reslt and run the test suite.
    testResult = unittest.TestResult()
    test_suite.run(testResult)
    print(testResult)


# Run all test functions in the specified test case class, the function parameter must be a class name not the class name string.
def run_all_test_in_class_generate_html_report(test_case_class):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()

    # Make all test function
    test = unittest.makeSuite(test_case_class)
    test_suite.addTest(test)

    # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)


# Run all test functions in the specified test case class, the function parameter must be a class name not the class name string.
def run_all_test_in_class_generate_xml_report(test_case_class):
    # Create a TestSuite object.
    test_suite = unittest.TestSuite()
    # Make all test function
    test = unittest.makeSuite(test_case_class)
    test_suite.addTest(test)
    # Create HtmlTestRunner object and run the test suite.
    test_runner = xmlrunner.XMLTestRunner(output=xml_report_dir)
    test_runner.run(test_suite)


def run_test_in_multiple_module_file():
    # Create test suite.
    test_suite = unittest.TestSuite()
    # Load all test case class in current folder.
    all_test_cases = unittest.defaultTestLoader.discover('.', '*.py')
    # Loop the found test cases and add them into test suite.
    for test_case in all_test_cases:
        test_suite.addTests(test_case)

        # Create a test reslt and run the test suite.
    testResult = unittest.TestResult()
    test_suite.run(testResult)
    print(testResult)


def run_test_in_multiple_module_file_generate_html_report():
    # Create test suite.
    test_suite = unittest.TestSuite()
    # Load all test case class in current folder.
    all_test_cases = unittest.defaultTestLoader.discover('.', '*.py')
    # Loop the found test cases and add them into test suite.
    for test_case in all_test_cases:
        test_suite.addTests(test_case)

        # Create HtmlTestRunner object and run the test suite.
    test_runner = HtmlTestRunner.HTMLTestRunner(output=html_report_dir)
    test_runner.run(test_suite)


def run_test_in_multiple_module_file_generate_xml_report():
    # Create test suite.
    test_suite = unittest.TestSuite()
    # Load all test case class in current folder.
    all_test_cases = unittest.defaultTestLoader.discover('.', '*.py')
    # Loop the found test cases and add them into test suite.
    for test_case in all_test_cases:
        test_suite.addTests(test_case)

        # Create HtmlTestRunner object and run the test suite.
    test_runner = xmlrunner.XMLTestRunner(output=xml_report_dir)
    test_runner.run(test_suite)

'''
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=html_report_dir))
    #run_all_test_generate_html_report()
    #run_all_test()
    # run_all_test_generate_xml_report()
    # run_test_suite('test_function_one')
    # run_test_suite_generate_html_report('test_function_two')
    # run_test_suite_generate_xml_report('test_function_two')
    # run_all_test_in_class(HtmlReportExample)
    # run_all_test_in_class_generate_html_report(HtmlReportExample)
    # run_all_test_in_class_generate_xml_report(HtmlReportExample)
    # run_test_in_multiple_module_file()
    # run_test_in_multiple_module_file_generate_html_report()
    # run_test_in_multiple_module_file_generate_xml_report()