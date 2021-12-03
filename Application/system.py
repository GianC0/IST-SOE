from gui import GUI
from gui import MODES
from aggregator import Aggregator
from evaluator import Evaluator
from datetime import datetime

def is_date(string):
    fmt = '%Y-%m-%d'
    try:
        datetime.strptime(string, fmt)
        return True, ''
    except ValueError as e:
        return False, str(e)
    
class System():

    def __init__(self):
        
        self.aggregator = Aggregator()
        self.allData = self.aggregator.get_data()
        self.sensorLocations = self.aggregator.get_locations()

        self.GUI = GUI(self.sensorLocations)

        self.evaluator = Evaluator(self.allData)

    def spot_error(self):#recognize errors: returns string of description of the error if present, '' if absent
        mode = self.form['Mode']
        d1 = self.form['Date1']
        d2 = self.form['Date2']
        s1 = self.form['Loc1'].split(':')[0]
        s2 = self.form['Loc2'].split(':')[0]
        
        if d1 != 'empty':
            (flag,mex) = is_date(d1)
            if flag == False:
                return 'Data field 1 is not correct: \n'+mex
        if d2 != 'empty':
            if d1 == 'empty':
                return 'Inserted a final date but not an initial one!'
            (flag,mex) = is_date(d2)
            if flag == False:
                return 'Data field 2 is not correct: '+mex
            if d2 <= d1:
                return 'Data field 2 must be after than data field 1!'
            
        if (s1 == 'empty' or s2 == 'empty') and mode == MODES[4]:
            return 'Location fields have not been selected!'

        if s2 != 'empty' and mode != MODES[4]:
            return 'Location field 2 should not be filled for this function!'

        if mode == MODES[4] and s2 == s1:
            return 'Locations selected must be different!'

        if s1 == 'empty' and mode == MODES[3]:
            return 'Location field 1 has not been selected!'

        if mode == MODES[1]:
            if d1 == 'empty':
                return 'Data field 1 has not been inserted!'
            if s1 == 'empty':
                return 'Location field 1 has not been selected!'

        if (mode == MODES[2] or mode == MODES[4]) and d1 == 'empty':
            return 'Data field 1 has not been inserted!'

        if mode == MODES[2] and s1 != 'empty':
            return 'Location field 1 should not be filled for this function!'
        return ''

    def run(self):
        self.form = {'Mode':'','Date1':'','Date2':'','Loc1':'','Loc2':''}#form to be passed to gui to retrieve user's data
        end = False
        while end is False:

            if self.GUI.is_defined() == True:
                self.GUI.show(self.form)
            else:
                break
            print(self.form)
            error = self.spot_error()

            result = -1
            if error == '':#compute the result calling the evaluator only if no error
                result = self.evaluator.get_result(self.form)

            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                end = self.GUI.showResult(result,error,self.form['Mode'])
            else:
                break
    