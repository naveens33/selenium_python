import unittest
from ddt import ddt, data

@ddt
class TestDDTData(unittest.TestCase):

    @data(56, 26, 56, 39, 17)
    def test_withddtdata(self, x):
        self.assertGreater(x, 50)
