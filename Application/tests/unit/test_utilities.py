import unittest
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(os.path.dirname(currentdir))
sys.path.append(parentdir)
from utilities import get_latitude,get_longitude,is_date,getEntry,getList,delete,spot_error

class TestUtilities(unittest.TestCase):

    def test_get_latitude(self):
        lat = 0
        self.assertEqual(get_latitude(lat), '0.00° E')
        lat = -25.6
        self.assertEqual(get_latitude(lat), '25.60° W')
        lat = 50.146
        self.assertEqual(get_latitude(lat), '50.15° E')
        lat = 110.2
        with self.assertRaises(ValueError):
            get_latitude(lat)

    def test_get_longitude(self):
        long = 0
        self.assertEqual(get_longitude(long), '0.00° N')
        long = -25.6
        self.assertEqual(get_longitude(long), '25.60° S')
        long = 50.146
        self.assertEqual(get_longitude(long), '50.15° N')
        long = 190.2
        with self.assertRaises(ValueError):
            get_longitude(long)

    def test_is_date(self):
        date = 'abcd203mv'
        self.assertFalse(is_date(date)[0])
        date = '1980-03-25'
        self.assertTrue(is_date(date)[0])
        date = '10-10-2000'
        self.assertFalse(is_date(date)[0])
        date = '1980-30-10'
        self.assertFalse(is_date(date)[0])
        date = '2021-02-31'
        self.assertFalse(is_date(date)[0])
        date = '2015-1-1'
        self.assertTrue(is_date(date)[0])
        date = '2015/1/1'
        self.assertFalse(is_date(date)[0])

    def test_spot_error(self):
        min_date = '2010-10-10'
        max_date = '2020-01-01'
        form = {'Mode':'','Date1':'empty','Date2':'empty','Loc1':'empty','Loc2':'empty'}

        form['Mode'] = 'Air Quality'
        self.assertEqual(spot_error(form,min_date,max_date),'Date field 1 has not been inserted!')
        form['Date1'] = '2009-06-10'
        self.assertEqual(spot_error(form,min_date,max_date),'Date field 1 out of the range registered')
        form['Date1'] = '2021-06-10'
        self.assertEqual(spot_error(form,min_date,max_date),'Date field 1 out of the range registered')
        form['Date1'] = '2015-08-30'
        self.assertEqual(spot_error(form,min_date,max_date),'Location field 1 has not been selected!')
        form['Loc1'] = 'Sensor4'
        self.assertEqual(spot_error(form,min_date,max_date),'')
        form['Loc2'] = 'Sensor5'
        self.assertEqual(spot_error(form,min_date,max_date),'Location field 2 should not be filled for this function!')
        form['Loc2'] = 'empty'
        form['Date2'] = '2014-10-10'
        self.assertEqual(spot_error(form,min_date,max_date),'Date field 2 must be after than date field 1!')

        form['Mode'] = 'Sensor Similarity'
        form['Date1'] = '2013-12-10'
        form['Loc1'] = 'Sensor5';form['Loc2'] = 'empty';form['Date2'] = 'empty'
        self.assertEqual(spot_error(form,min_date,max_date),'Location field 1 should not be filled for this function!')
        form['Loc1'] = 'empty'
        self.assertEqual(spot_error(form,min_date,max_date),'')

        form['Mode'] = 'Location Comparison'
        self.assertEqual(spot_error(form,min_date,max_date),'Location fields have not been selected!')
        form['Loc1'] = 'Sensor9';form['Loc2'] = 'Sensor9'
        self.assertEqual(spot_error(form,min_date,max_date),'Locations selected must be different!')

    def runTest(self):
        self.test_get_latitude()
        self.test_get_longitude()
        self.test_is_date()
        self.test_spot_error()

if __name__ == '__main__':
    unittest.main()