import unittest
from ddt import ddt, file_data

@ddt
class TestDDTDataFileDict(unittest.TestCase):

    @file_data('datafiledict.json')
    def test_with_ddt_file_data_dict(self, username,password):
        print(username,password)