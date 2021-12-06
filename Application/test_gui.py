import unittest
from gui import GUI

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.gui = GUI()

    def tearDown(self):
        self.gui = None

    def test(self):
        return

    def runTest(self):
        return

if __name__ == '__main__':
    unittest.main()