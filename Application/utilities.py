import sys, os
from datetime import datetime
from pathlib import Path
from tkinter import TclError
from tkinter.constants import  END

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("assets")
MODES = {1:'Air Quality', 2:'Sensor Similarity',3:'Characterising Values',4:'Location Comparison'} 

def relative_to_assets(path: str) -> Path:
        return resource_path(ASSETS_PATH / Path(path))
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)
def getEntry(entry):
    x = entry.get()
    if x == '':
        return 'empty'
    return x
def getList(listbox):
    x = 'empty'
    try: 
        index = listbox.curselection()
        x = listbox.get(index)
    except TclError:
        pass
    return x
def delete(entry1,entry2,listbox1,listbox2):
    entry1.delete(0,END)
    entry2.delete(0,END)
    listbox1.selection_clear(0,END)
    listbox2.selection_clear(0,END)
    return
def get_latitude(lat):
    if abs(lat) > 90:
        raise ValueError('Wrong latitude value')
    if lat < 0:
        dir = 'W'
    else:
        dir = 'E'
    lat = abs(lat)
    return '{:.2f}° '.format(lat) + dir
def get_longitude(long):
    if abs(long) > 180:
        raise ValueError('Wrong longitude value')
    if long < 0:
        dir = 'S'
    else:
        dir = 'N'
    long = abs(long)
    return '{:.2f}° '.format(long) + dir
def is_date(string):
    fmt = '%Y-%m-%d'
    try:
        datetime.strptime(string, fmt)
        return True, ''
    except ValueError as e:
        return False, str(e)

def spot_error(form,min_date,max_date):#recognize errors: returns string of description of the error if present, '' if absent
    mode = form['Mode']
    d1 = form['Date1']
    d2 = form['Date2']
    s1 = form['Loc1'].split(':')[0]
    s2 = form['Loc2'].split(':')[0]
    
    if d1 == 'empty':
        return 'Date field 1 has not been inserted!'
    (flag,mex) = is_date(d1)
    if flag == False:
        return 'Date field 1 is not correct: \n'+mex
    if datetime.strptime(d1,'%Y-%m-%d') < datetime.strptime(min_date,'%Y-%m-%d') \
         or datetime.strptime(d1,'%Y-%m-%d') > datetime.strptime(max_date,'%Y-%m-%d'):
        return 'Date field 1 out of the range registered'
    if d2 != 'empty':
        (flag,mex) = is_date(d2)
        if flag == False:
            return 'Date field 2 is not correct: '+mex
        if datetime.strptime(d2,'%Y-%m-%d') <= datetime.strptime(d1,'%Y-%m-%d'):
            return 'Date field 2 must be after than date field 1!'
        if datetime.strptime(d2,'%Y-%m-%d') > datetime.strptime(max_date,'%Y-%m-%d'):
            return 'Date field 2 out of the range registered'
        
    if (s1 == 'empty' or s2 == 'empty') and mode == MODES[4]:
        return 'Location fields have not been selected!'
    if s2 != 'empty' and mode != MODES[4]:
        return 'Location field 2 should not be filled for this function!'
    if mode == MODES[4] and s2 == s1:
        return 'Locations selected must be different!'
    if s1 == 'empty' and (mode == MODES[3] or mode == MODES[1]):
        return 'Location field 1 has not been selected!'
    if mode == MODES[2] and s1 != 'empty':
        return 'Location field 1 should not be filled for this function!'
    return ''