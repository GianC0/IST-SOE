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
def is_date(string):
    fmt = '%Y-%m-%d'
    try:
        datetime.strptime(string, fmt)
        return True, ''
    except ValueError as e:
        return False, str(e)
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
