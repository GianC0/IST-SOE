from gui import GUI

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
        #recognize errors...
        #returns string of description of the error if present, '' if absent
        return ''

    def run(self):
        end = False
        while end is False:

            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                self.GUI.show(self.form)
            else:
                break

            error = self.spot_error()
            result = -1
            if error == '':
                result = 0 #compute the result calling the evaluator


            if self.GUI.is_defined() == True:#check that the user hasn't forced the closure of the window
                end = self.GUI.showResult(result,error,self.form['Mode'])
            else:
                break
    