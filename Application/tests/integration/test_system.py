import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
from system import System
from gui import GUI
from aggregator import Aggregator
from evaluator import Evaluator

class TestSystem(unittest.TestCase):

    def setUp(self):
        self.aggregator = Aggregator()

    def tearDown(self):
        self.system = None
        self.aggregator = None
        self.evaluator = None

    def test_integration_aggregator_evaluator(self):
        data = self.aggregator.get_data()
        self.assertIsNotNone(data)
        self.evaluator = Evaluator(data)

        form = {'Mode':'Air Quality','Date1':'2017-05-15','Date2':'2017-05-17','Loc1':'Sensor6: 23.63° W, 71.25° S','Loc2':'empty'}
        result = self.evaluator.get_result(form)
        self.assertEqual(result,'Very Poor')

        form = {'Mode':'Characterising Values','Date1':'2017-12-12','Date2':'empty','Loc1':'Sensor0: 8.16° W,37.66° S','Loc2':'empty'}
        result = self.evaluator.get_result(form)
        self.assertAlmostEqual(result['Value'][2],55.46,places=2)

    def test_system_integration(self):
        self.system = System()
        self.assertIsNotNone(self.system)

        form = {'Mode':'Sensor Similarity','Date1':'empty','Date2':'empty','Loc1':'empty','Loc2':'Sensor3:'}
        self.assertEqual(self.system.run(form,testing=True),'Date field 1 has not been inserted!')

        form = {'Mode':'Location Comparison','Date1':'2017-10-10','Date2':'2017-12-10','Loc1':'Sensor2:','Loc2':'Sensor1:'}
        self.assertEqual(self.system.run(form,testing=True).split('\n')[0],'Sensor2: SO2: Moderate, NO2: Very Poor, O3: Poor, PM10: Poor')

        form = {'Mode':'Location Comparison','Date1':'2017-10-10','Date2':'2017-10-11','Loc1':'Sensor2:','Loc2':'Sensor2:'}
        self.assertEqual(self.system.run(form,testing=True),'Locations selected must be different!')

        form = {'Mode':'Sensor Similarity','Date1':'2017-09-09','Date2':'2017-09-10','Loc1':'empty','Loc2':'empty'}
        self.assertEqual(self.system.run(form,testing=True).split('\n')[0].split(':')[1],' [Sensor0, Sensor3]')

        form = {'Mode':'Air Quality','Date1':'2026-30-20','Date2':'202','Loc1':'Sensor4:','Loc2':'empty'}
        self.assertEqual(self.system.run(form,testing=True).split(':')[0],'Date field 1 is not correct')
    
    def runTest(self):
        self.test_integration_aggregator_evaluator()
        self.test_system_integration()

if __name__ == '__main__':
    unittest.main() 