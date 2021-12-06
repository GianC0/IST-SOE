import unittest
from system import System

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.system = System()

    def tearDown(self):
        self.system = None

    def test(self):
        return

    def runTest(self):
        return

if __name__ == '__main__':
    unittest.main()