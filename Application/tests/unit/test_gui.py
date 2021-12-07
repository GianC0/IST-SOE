import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
from gui import GUI

class TestGUI(unittest.TestCase):

    def setUp(self):
        self.loc = ['Sensor0,Sensor1,Sensor2']
        self.gui = GUI(self.loc)

    def test_window(self):
        self.gui.close_window()
        self.assertFalse(self.gui.is_defined())

    def runTest(self):
        self.test_window()

if __name__ == '__main__':
    unittest.main() 