import unittest

class TestCase2(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        print("setUpClass")

    def setUp(self):
        print("setUP")
        currentTest = self.id().split('.')[-1]
        if currentTest == 'test_method6':
            self.skipTest('reason for skipping')

        def cleanup_a():
            print("cleanup_a")
        self.addCleanup(cleanup_a)

    def test_method5(self):
        print("test method5")
        def cleanup_b():
            print("cleanup_b")
        self.addCleanup(cleanup_b)

    def test_method6(self):
        print("test method6")

    def tearDown(self):
        print("tearDown")
        def cleanup_c():
            print("cleanup_c")
        self.addCleanup(cleanup_c)

if __name__ == '__main__':
    unittest.main()