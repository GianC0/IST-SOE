from gui import GUI

class System():

    def __init__(self):
        #call method to retrieve data from aggregator
        self.allData = -1
        #extract locations to give to GUI
        self.sensorLocations = [1,2,3,4,5,6,7,8,9]
        self.GUI = GUI(self.sensorLocations)
        self.form = {'Mode':'','Date1':'','Date2':'','Loc1':'','Loc2':''}#form to be passed to gui to retrieve user's data

    def run(self):
        self.GUI.show(self.form)
        print(self.form)
        #use self.form to compute the result
        result = 'ciao'
        self.GUI.showResult(result)
    