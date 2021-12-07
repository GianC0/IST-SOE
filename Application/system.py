from gui import GUI
from aggregator import Aggregator
from evaluator import Evaluator
from utilities import spot_error

class System():

    def __init__(self):
        
        self.aggregator = Aggregator()
        self.allData = self.aggregator.get_data()
        self.sensorLocations = self.aggregator.get_locations()

        self.min_date, self.max_date = self.aggregator.get_period()

        self.GUI = GUI(self.sensorLocations)

        self.evaluator = Evaluator(self.allData)

    def run(self, arg=None, testing=False):
        #testing part that bypass the gui
        if testing is True:
            error = spot_error(arg,self.min_date,self.max_date)
            if error == '':
                return self.evaluator.get_result(arg)
            return error

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
    