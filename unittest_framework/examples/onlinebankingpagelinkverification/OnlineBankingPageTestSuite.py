import unittest
from unittest_framework.examples.onlinebankingpagelinkverification import OnlineBankingLinkVerificationBLogin
import OnlineBankingLinkVerificationALogin

tc1 = unittest.TestLoader().loadTestsFromTestCase(OnlineBankingLinkVerificationBLogin.TestCase)
tc2 = unittest.TestLoader().loadTestsFromTestCase(OnlineBankingLinkVerificationALogin.TestCase)

test_suite = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner().run(test_suite)