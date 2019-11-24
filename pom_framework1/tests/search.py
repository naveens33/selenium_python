import unittest
from pom_framework1.pages.homepage import HomePage


class Search(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        home=HomePage()
        home.do_search("Account")
        pass

    def setUp(self):
        pass

    def test(self):
        pass

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        pass