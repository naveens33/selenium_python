import unittest

class TestWithoutDDT(unittest.TestCase):

    def testwithoutddt(self):
        for x in [56, 26, 56, 39, 17]:
            self.assertGreater(x, 50)