import unittest

class TestWithoutDDT(unittest.TestCase):

    def test_withoutddt(self):
        for x in [56, 26, 56, 39, 17]:
            self.assertGreater(x, 50)