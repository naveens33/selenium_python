import unittest

class TestWithoutDDT(unittest.TestCase):

    def test_withoutddt(self):
        li=[56, 26, 56, 39, 17]
        for x in li:
            self.assertGreater(x, 50)