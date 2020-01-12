import unittest
from ddt import ddt, data, unpack

@ddt
class TestDDTUnpack(unittest.TestCase):

    @data(('uname1', 'pword1'), ('uname2', 'pword2'))
    @unpack
    def testddtunpack(self, uname, pword):
        print("User Name: "+uname)
        print("Password: " + pword)