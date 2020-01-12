import unittest
from ddt import ddt, file_data

@ddt
class TestDDTDataFile(unittest.TestCase):

    @file_data('datafile.json')
    def test_with_ddt_file_data(self, x):
        self.assertGreater(x, 50)
