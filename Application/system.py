from gui import GUI
from dateutil.parser import parse
from gui import MODES
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
        #call method to retrieve data from aggregator
        self.allData = -1
        #extract locations to give to GUI
        self.sensorLocations = [1,2,3,4,5,6,7,8,9]
        self.GUI = GUI(self.sensorLocations)
        self.form = {'Mode':'','Date1':'','Date2':'','Loc1':'','Loc2':''}#form to be passed to gui to retrieve user's data
        self.aggregator = 0
        self.evaluator = 0

    def spot_error(self):
        #recognize errors: returns string of description of the error if present, '' if absent
        if self.form['Date1'] != 'empty':
            (flag,mex) = is_date(self.form['Date1'])
            if flag == False:
                return 'Data field 1 is not correct: \n'+mex
        if self.form['Date2'] != 'empty': 
            (flag,mex) = is_date(self.form['Date2'])
            if flag == False:
                return 'Data field 2 is not correct: '+mex

        if self.form['Loc1'] == 'empty' or self.form['Loc2']=='empty' and self.form['Mode']==MODES[4]:
            return 'Location fields have not been selected!'

        if self.form['Loc2'] != 'empty' and self.form['Mode'] != MODES[4]:
            return 'Location field 2 should not be filled for this function!'

        if self.form['Loc1'] == 'empty' and self.form['Mode']==MODES[3]:
            return 'Location field 1 has not been selected!'

        if self.form['Mode'] == MODES[1]:
            if self.form['Date1'] == 'empty':
                return 'Data field 1 has not been inserted!'
            if self.form['Loc1'] == 'empty':
                return 'Location field 1 has not been selected!'

        if self.form['Mode'] == MODES[2] and self.form['Date1'] == 'empty':
            return 'Data field 1 has not been inserted!'

        return ''

    def run(self):
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
                result = 0 


            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                end = self.GUI.showResult(result,error,self.form['Mode'])
            else:
                break
    