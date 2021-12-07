from gui import GUI
from aggregator import Aggregator
from evaluator import Evaluator
from datetime import datetime
from utilities import is_date,spot_error,MODES

class System():

    def __init__(self):
        
        self.aggregator = Aggregator()
        self.allData = self.aggregator.get_data()
        self.sensorLocations = self.aggregator.get_locations()

        self.min_date, self.max_date = self.aggregator.get_period()

        self.GUI = GUI(self.sensorLocations)

        self.evaluator = Evaluator(self.allData)

    def run(self):
        self.form = {'Mode':'','Date1':'','Date2':'','Loc1':'','Loc2':''}#form to be passed to gui to retrieve user's data
        end = False
        while end is False:

            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                self.GUI.show(self.form)
            else:
                break
            
            error = spot_error(self.form, self.min_date, self.max_date)

            result = -1
            if error == '':#compute the result calling the evaluator only if no error
                result = self.evaluator.get_result(self.form)

            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                end = self.GUI.showResult(result,error,self.form['Mode'])
            else:
                break
    