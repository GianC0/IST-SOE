import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
from aggregator import Aggregator

class TestAggregator(unittest.TestCase):

    def setUp(self):
        self.aggregator = Aggregator()

    def tearDown(self):
        self.aggregator = None

    def test_get_data(self):
        data = self.aggregator.get_data()
        self.assertEqual(len(data),10)#verify the number of sensors detected
        count = 0
        for x in data.items():
            count += len(x[1])
        self.assertEqual(count,698880)#verify the number of entries loaded

    def test_get_locations(self):
        locations = self.aggregator.get_locations()
        self.assertEqual(len(locations),10)
        self.assertEqual(locations[4],'Sensor4: 10.05° W, 87.55° N')#check a random entry if it's correct

    def test_get_period(self):
        min,max = self.aggregator.get_period()
        self.assertEqual(min,'2017-01-02')
        self.assertEqual(max,'2017-12-31')

    def runTest(self):
        self.test_get_data()
        self.test_get_locations()
        self.test_get_period()

if __name__ == '__main__':
    unittest.main() 