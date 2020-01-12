import unittest
from ddt import ddt, idata


def data_generator():
    for x in [56, 26, 56, 39, 17]:
        yield x

@ddt
class TestDDTFuncGenerator(unittest.TestCase):

    @idata(data_generator())
    def testddtfuncgenerator(self, x):
        self.assertGreater(x, 50)
