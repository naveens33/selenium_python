import unittest
from unittest_framework.unittest_TC1 import TestCase1
from unittest_TC2 import TestCase2

tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCase1)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCase2)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([tc1, tc2])

# run the suite
unittest.TextTestRunner().run(test_suite)