import unittest
from unittest_framework.unittest_TC1 import TestCase1,TestCase3
from unittest_framework.unittest_TC2  import TestCase2

loader=unittest.TestLoader()
tc1 = loader.loadTestsFromTestCase(TestCase1)
tc2 = loader.loadTestsFromTestCase(TestCase2)
tc3 = loader.loadTestsFromTestCase(TestCase3)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([tc1, tc2, tc3])

# run the suite
unittest.TextTestRunner().run(test_suite)