import unittest
from ddt import ddt, idata


def firstname():
    for x in ["dhoni", "sachin", "kholi", "raina", "ashwin"]:
        yield x

@ddt
class TestDDTFuncGenerator(unittest.TestCase):

    @idata(firstname())
    def testddtfuncgenerator(self, x):
        print(x)