import unittest
from pandas import DataFrame
import os, sys
import pandas as pd
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
from evaluator import Evaluator
from utilities import resource_path

class TestEvaluator(unittest.TestCase):

    def setUp(self):
        try:
            self.df = pd.read_csv(resource_path('data/data.csv'))
            self.df['Timestamp'] = pd.to_datetime(self.df['Timestamp'])
            self.sens_list = pd.read_csv(resource_path('data/sensors.csv'))['SensorID']
            self.data = {}
            for s in self.sens_list:
                self.data[s] = self.df[self.df['SensorID'] == s]
        
            self.evaluator = Evaluator(self.data)
        except Exception as e:
            print(e)

    def tearDown(self):
        self.evaluator = None
        self.df = None
        self.data = None
        self.sens_list = None

    def test_get_aqi(self):
        form = {'Mode':'Air Quality','Date1':'2017-03-02','Date2':'2017-03-03','Loc1':'Sensor4: 10.05° W, 87.55° N','Loc2':'empty'}
        result = self.evaluator.get_result(form)
        self.assertNotEqual(result,'Poor')

    def test_get_similarity(self):
        form = {'Mode':'Sensor Similarity','Date1':'2017-06-25','Date2':'2017-06-30','Loc1':'empty','Loc2':'empty'}
        result = self.evaluator.get_result(form)
        self.assertEqual(result,'Similarity Group: [Sensor0, Sensor2, Sensor4, Sensor7]\n'\
            + 'Values: SO2: Moderate, NO2: Very Poor, O3: Poor, PM10: Poor\n\n' \
                + 'Similarity Group: [Sensor1, Sensor3, Sensor5, Sensor6, Sensor8, Sensor9]\n'\
            + 'Values: SO2: Moderate, NO2: Very Poor, O3: Poor, PM10: Moderate\n\n' )

    def test_get_char_data(self):
        form = {'Mode':'Characterising Values','Date1':'2017-01-02','Date2':'empty','Loc1':'Sensor0: 8.16° W,37.66° S','Loc2':'empty'}
        result = self.evaluator.get_result(form)
        self.assertIsInstance(result,DataFrame)
        self.assertAlmostEqual(result['Value'][0],243.122757,places=3)

    def test_get_comparison(self):
        form = {'Mode':'Location Comparison','Date1':'2017-10-10','Date2':'2017-10-13','Loc1':'Sensor4: 10.05° W, 87.55° N','Loc2':'Sensor6: 23.63° E, 71.25° S'}
        result = self.evaluator.get_result(form)
        self.assertEqual(result,'Sensor4: SO2: Moderate, NO2: Very Poor, O3: Poor, PM10: Moderate\n' \
                    + 'Sensor6: SO2: Moderate, NO2: Very Poor, O3: Poor, PM10: Poor')

    def runTest(self):
        self.test_get_char_data()
        self.test_get_aqi()
        self.test_get_comparison()
        self.test_get_similarity()

if __name__ == '__main__':
    unittest.main()