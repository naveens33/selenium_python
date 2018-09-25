import unittest
from ddt import ddt, data, idata, file_data, unpack

@ddt
class TestDDTData(unittest.TestCase):

    @data(56, 26, 56, 39, 17)
    def testwithddtdata(self, x):
        self.assertGreater(x, 50)