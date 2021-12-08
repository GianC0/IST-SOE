import pandas as pd
from utilities import MODES

class Evaluator:

    def __init__(self, data):
        self.data = data  # dictionary

    def get_result(self,form):
        mode = form['Mode']
        d1 = form['Date1']
        d2 = form['Date2']
        s1 = form['Loc1'].split(':')[0]
        s2 = form['Loc2'].split(':')[0]

        if mode == MODES[1]:
            return 'The AQI is ' + self.__get_aqi(s1,d1,d2)
        elif mode == MODES[2]:
            return self.__get_similarity(d1,d2)
        elif mode == MODES[3]:
            return self.__get_charData(s1,d1,d2).to_string()
        return self.__get_comparison(s1,s2,d1,d2)

    def __get_charData(self, sensor, dateI, dateF):

        # controllo su 1 o 2 input
        if dateF == 'empty':
            start_date = pd.to_datetime(dateI) - pd.Timedelta("1 days")
            end_date = pd.to_datetime(dateI)
        else:
            start_date = pd.to_datetime(dateI)
            end_date = pd.to_datetime(dateF)

        data = self.data[sensor]

        mask = (data['Timestamp'] >= start_date) & (data['Timestamp'] <= end_date) & (data['SensorID'] == sensor)
        data = data.loc[mask][['AttributeID', 'Value']]  # Dataframe of 2 columns Attribute ID, value

        # calcola il val medio per ogni gas
        data = data.groupby('AttributeID', axis=0).mean().reset_index()
        data.sort_values(by='AttributeID')
        data = data.assign(
            Description=['µg/m3 nitrogen dioxide content', 'µg/m3 ozone content', 'µg/m3 fine particles content',
                         'µg/m3 sulfur dioxide content'])
        return data  # struct: AttributeID,Description,Value,unit,

    def __get_similarity(self, dateI, dateF):
        sens_list = 'Sensor0,Sensor1,Sensor2,Sensor3,Sensor4,Sensor5,Sensor6,Sensor7,Sensor8,Sensor9'.split(',')
        data = {'Sensor':[],'String':[]}
        out = {}
        out_str = ''
        for s in sens_list:
            data['Sensor'].append(s)
            data['String'].append( str((self.__get_aqi(s,dateI,dateF,all_aqi_val=True)) ))
        data = pd.DataFrame(data,columns=['Sensor','String'])
        groups = data['String'].drop_duplicates()

        for _, group in groups.iteritems():
            out[str(group)] = []
            for index,row in data['String'].iteritems():
                if group == row and 'Sensor'+str(index) not in out[str(group)]:
                    out[str(group)].append('Sensor'+str(index))

        for k,v in out.items():
            if len(v)>1:
                out_str += 'Similarity Group: '+str(v)+'\nValues: '+str(k)+'\n\n'

        if out_str == '':
            out_str = 'No similarity between sensors has been found in the selected period!'

        return out_str.replace('{','').replace('}','').replace("'",'')

    def __get_aqi(self, sensor, dateI, dateF, all_aqi_val=False):

        # EUROPEAN AQI-VALUES LABELS December 2021

        scores = ['Good', 'Fair', 'Moderate', 'Poor', 'Very Poor', 'Extremely Poor']
        gases_thres = {'SO2': [(0, 100), (100, 200), (200, 350), (350, 500), (500, 750), (750, 9999)],
                       'NO2': [(0, 40), (40, 90), (90, 120), (120, 230), (230, 340), (340, 9999)],
                       'O3': [(0, 50), (50, 100), (100, 130), (130, 240), (240, 380), (380, 9999)],
                       'PM10': [(0, 20), (20, 40), (40, 50), (50, 100), (100, 150), (150, 9999)]}

        data = self.__get_charData(sensor, dateI, dateF)
        data = data[['AttributeID', 'Value']]
        aqi = {'SO2': 0, 'NO2': 0, 'O3': 0, 'PM10': 0}
        for _, row in data.iterrows():
            gas = row[0]
            value = row[1]
            for interval in gases_thres[gas]:
                if interval[0] <= value < interval[1]:
                    if gases_thres[gas].index(interval) > aqi[gas]:
                        aqi[gas] = gases_thres[gas].index(interval)
                    break

        # useful for similarity comparison
        if all_aqi_val:
            for key,_ in aqi.items():
                aqi[key] = scores[aqi[key]]
            return aqi

        return scores[max(aqi.values())]

    def __get_comparison(self, s1, s2, dateI, dateF):
        aq1 = self.__get_aqi(s1, dateI, dateF, all_aqi_val=True)
        aq2 = self.__get_aqi(s2, dateI, dateF, all_aqi_val=True)

        return  s1 + ': '+ str(aq1).replace('{','').replace('}','').replace("'",'')+\
                '\n' + s2 + ': ' + str(aq2).replace('{','').replace('}','').replace("'",'')
