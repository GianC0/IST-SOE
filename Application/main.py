from system import System

def startApp():
    sys = System()
    sys.run()


if __name__ == '__main__':
    startApp()


#problems to be fixed:
#-location comparison -> errors nan or KeyError
#-sensor similarity->nan or KeyError