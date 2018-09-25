import unittest
from ddt import ddt, data, unpack

@ddt
class TestDDTUnpack(unittest.TestCase):

    @data(('Sachin', 4), ('Dhoni', 8))
    @unpack
    def testddtunpack(self, name, rank):
        print("Student Name: "+name)
        print("Rank: " + str(rank))