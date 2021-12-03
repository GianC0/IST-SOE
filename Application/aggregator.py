from datetime import timedelta
import pandas as pd

def get_latitude(lat):
    if lat < 0:
        dir = 'W'
    else:
        dir = 'E'
    lat = abs(lat)
    return '{:.2f}° '.format(lat) + dir
def get_longitude(long):
    if long < 0:
        dir = 'S'
    else:
        dir = 'N'
    long = abs(long)
    return '{:.2f}° '.format(long) + dir

class Aggregator:

    def __init__(self):
        self.data = pd.read_csv('data/data.csv')
        self.data['Timestamp'] = pd.to_datetime(self.data['Timestamp'])
        self.sensors = pd.read_csv('data/sensors.csv')

    def get_data(self):
        return self.__aggregate()

    def get_locations(self):
        
        len = self.sensors.shape[0]
        locations = [''] * len
        for i in range(len):
            locations[i] = self.sensors['SensorID'][i] + ': ' + get_latitude(self.sensors['Latitude'][i]) + \
                ', ' + get_longitude(self.sensors['Longitude'][i])

        return locations

    def get_period(self):
        min = self.data['Timestamp'].min() + timedelta(days=1)#functions consider the day before!
        max = self.data['Timestamp'].max() + timedelta(days=1)
        min = str(min).split(' ')[0]
        max = str(max).split(' ')[0]
        return min,max

    def __aggregate(self):
        sens_list = self.sensors['SensorID']
        data = {}
        for s in sens_list:
            data[s] = self.data[self.data['SensorID'] == s]
        return data


