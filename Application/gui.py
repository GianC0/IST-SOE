from pathlib import Path
from PIL import ImageTk, Image
from tkinter import Label, Tk, Canvas, Button, PhotoImage, Entry,ttk,Listbox,TclError
import tkinter
from tkinter.constants import ANCHOR, END
from pandas import DataFrame

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
MODES = {1:'Air Quality', 2:'Sensor Similarity',3:'Characterising Values',4:'Location Comparison'} 

def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)
        
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


    return
def generate_result(result,window,usecase,error,color):
    c = Canvas(
            window,
            height = 400,
            width = 850,
            bg=color,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )
    c.place(x=30,y=150)
    if error != '':
        text = error
    elif usecase == MODES[1]:#AIR QUALITY
        #result should be a string
        text = result
    elif usecase == MODES[2]:#SENSOR SIMILARITY
        #result should be a string
        text = result
    elif usecase == MODES[3]:#CHARACTERISING VALUES
        #result should be a pd.DataFrame
        text = result.to_string()
    else:                   #LOCATION COMPARISON
        #result should be a string
        text = result
    c.create_text(
            40,
            160,
            anchor="nw",
            text=text,
            fill='#000000',
            font=("Roboto Bold", 25 * -1)
        )
    return

class GUI():

    def __createWindow(self):
        self.window = Tk()
        self.window.geometry("1440x780")
        self.window.resizable(False, False)
        self.window.title('Software for air quality analysis')
        self.icon = ImageTk.PhotoImage(Image.open('assets/logo.png'))
        self.window.iconphoto(True, self.icon)
        self.window.protocol("WM_DELETE_WINDOW", lambda: self.__close_window())
        return
    
    def __init__(self,locations):
        self.__createWindow()
        self.locations = locations
    
    def __close_window(self):
        self.window.destroy()
        self.window = -1
        return
    def is_defined(self):
        return self.window != -1


    def __cleanWindow(self):
        _list = self.window.winfo_children()
        for item in _list :
            if item.winfo_children() :
                _list.extend(item.winfo_children())
        
        for item in _list:
            item.destroy()
    
    def __submit(self,form,entry1,entry2,listbox1,listbox2):
        form['Date1'] = getEntry(entry1)
        form['Date2'] = getEntry(entry2)
        form['Loc1'] = getList(listbox1)
        form['Loc2'] = getList(listbox2)
    
        self.window.destroy()
        return

    def __home(self,form):
        self.__cleanWindow()
        self.show(form)
        return

    def __restart(self,mode,flag):
        self.window.destroy()
        if mode == 'exit':
            self.window = -1
            flag[0] = True
        self.window = -2
        return


    def show(self,form):

        if self.window == -1 or self.window == -2:
            self.__createWindow()

        bg = ImageTk.PhotoImage(Image.open('assets/back4.jpg').resize((1440, 780)))
        canvas = Canvas(
            self.window,
            height = 780,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        canvas.place(x = 0, y = 0)
        canvas.create_image(
            0.0,
            0.0,
            anchor='nw',
            image=bg)

        canvas.create_text(
            738.0,
            22.0,
            anchor="nw",
            text="Air quality analysis",
            fill="#FFFFFF",
            font=("Poiret One", 72 * -1)
        )

        canvas.create_text(
            119.0,
            760.0,
            anchor="nw",
            text="Demo v1.0\n",
            fill="#FFFFFF",
            font=("Roboto", 20 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_1.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.__showForm(1,form),
            relief="flat"
        )
        button_1.place(
            x=387.0,
            y=284.0,
            width=243.1182861328125,
            height=149.2493896484375
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_2.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.__showForm(2,form),
            relief="flat"
        )
        button_2.place(
            x=808.8817138671875,
            y=511.7506103515625,
            width=243.1182861328125,
            height=149.2493896484375
        )

        button_image_3 = PhotoImage(
            file=relative_to_assets("button_3.png"))
        button_3 = Button(
            image=button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.__showForm(3,form),
            relief="flat"
        )
        button_3.place(
            x=808.8817138671875,
            y=284.0,
            width=243.1182861328125,
            height=149.2493896484375
        )

        button_image_4 = PhotoImage(
            file=relative_to_assets("button_4.png"))
        button_4 = Button(
            image=button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda : self.__showForm(4,form),
            relief="flat"
        )
        button_4.place(
            x=387.0,
            y=511.7506103515625,
            width=243.1182861328125,
            height=149.2493896484375
        )

        canvas.create_text(
            1270.0,
            735.0,
            anchor="nw",
            text="Made by\nThe Marpions",
            fill="#FFFFFF",
            font=("RobotoSlab Regular", 18 * -1)
        )
    
        self.window.mainloop()
        return

    def __showForm(self,mode,form):
        self.__cleanWindow()
        form['Mode'] = MODES[mode]
        bg = ImageTk.PhotoImage(Image.open('assets/back5.jpg').resize((1440, 780)))
        canvas = Canvas(
            self.window,
            height = 780,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        canvas.place(x = 0, y = 0)
        canvas.create_image(
            0.0,
            0.0,
            anchor='nw',
            image=bg
        )
        canvas.create_rectangle(
            288.99999999999994,
            267.0,
            707.0,
            360.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            323.99999999999994,
            237.00000000000003,
            anchor="nw",
            text="Location",
            fill="#FFFFFF",
            font=("Roboto Bold", 24 * -1)
        )

        #Listbox values
        _list = tkinter.StringVar(value=self.locations)

        listbox1 = Listbox(self.window,listvariable=_list,font=('Helvetica bold',12),exportselection=False)
        listbox1.place(x=289.0,y=270.0,width=400,height=80)
        scrollbar1 = ttk.Scrollbar(self.window,orient='vertical',command=listbox1.yview)
        listbox1['yscrollcommand'] = scrollbar1.set
        scrollbar1.place(x=690.0,y=270.0,width=15,height=80)

        canvas.create_rectangle(
            868.0,
            267.0,
            1286.0,
            360.0,
            fill="#FFFFFF",
            outline="")

        canvas.create_text(
            885.0,
            237.00000000000003,
            anchor="nw",
            text="Location #2 (for comparison)",
            fill="#FFFFFF",
            font=("Roboto Bold", 24 * -1)
        )

        listbox2 = Listbox(self.window,listvariable=_list,font=('Helvetica bold',12),exportselection=False)
        listbox2.place(x=868.0,y=270.0,width=400,height=80)
        scrollbar2 = ttk.Scrollbar(self.window,orient='vertical',command=listbox2.yview)
        listbox2['yscrollcommand'] = scrollbar2.set
        scrollbar2.place(x=1270.0,y=270.0,width=15,height=80)


        entry_image_1 = PhotoImage(
            file=relative_to_assets("entry_1.png"))
        entry_bg_1 = canvas.create_image(
            497.99999999999994,
            504.5,
            image=entry_image_1
        )
        entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=('Arial', 20)
        )
        entry_1.place(
            x=318.99999999999994,
            y=458.0,
            width=358.0,
            height=91.0
        )

        canvas.create_text(
            323.99999999999994,
            426.0,
            anchor="nw",
            text="Date [yyyy-mm-dd]",
            fill="#FFFFFF",
            font=("Roboto Medium", 24 * -1)
        )

        entry_image_2 = PhotoImage(
            file=relative_to_assets("entry_2.png"))
        entry_bg_2 = canvas.create_image(
            1078.0,
            504.5,
            image=entry_image_2
        )
        entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font=('Roboto', 20)
        )
        entry_2.place(
            x=899.0,
            y=458.0,
            width=358.0,
            height=91.0
        )

        canvas.create_text(
            885.0,
            426.0,
            anchor="nw",
            text="Date #2 [yyyy-mm-dd] (for timespan)",
            fill="#FFFFFF",
            font=("Roboto Medium", 24 * -1)
        )

        canvas.create_text(
            744.0,
            26.00000000000003,
            anchor="nw",
            text="Enter the details.",
            fill="#FFFFFF",
            font=("Roboto Bold", 64 * -1)
        )

        button_image_5 = PhotoImage(
            file=relative_to_assets("button_5.png"))
        button_5 = Button(
            image=button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.__submit(form,entry_1,entry_2,listbox1,listbox2),
            relief="flat"
        )
        button_5.place(
            x=1168.0238037109375,
            y=687.5681762695312,
            width=213.757080078125,
            height=70.80682373046875
        )
        button_image_6 = PhotoImage(
            file=relative_to_assets("button_6.png"))
        button_6 = Button(
            image=button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: delete(entry_1,entry_2,listbox1,listbox2),
            relief="flat"
        )
        button_6.place(
            x=900.0,
            y=687.5681762695312,
            width=213.757080078125,
            height=70.80682373046875
        )
        button_image_7 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_7 = Button(
            image=button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.__home(form),
            relief="flat"
        )
        button_7.place(
            x=80.0,
            y=687.5681762695312,
            width=213.757080078125,
            height=70.80682373046875
        )
        self.window.mainloop()
        return

    def showResult(self,result,error,usecase):
        self.__createWindow()
        flag = [False]
        bg = ImageTk.PhotoImage(Image.open('assets/back8.jpg').resize((1440, 780)))
        canvas = Canvas(
            self.window,
            height = 780,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
            )

        canvas.place(x = 0, y = 0)
        canvas.create_image(
            0.0,
            0.0,
            anchor='nw',
            image=bg
        )

        if error == '':
            txt = 'Results.'
            color = '#FFFFFF'
        else:
            txt = 'Error!'
            color = '#FF0000'
        canvas.create_text(
            44.99999999999994,
            26.00000000000003,
            anchor="nw",
            text=txt,
            fill=color,
            font=("Roboto Bold", 64 * -1)
        )

        button_image_1 = PhotoImage(
            file=relative_to_assets("button_7.png"))
        button_1 = Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.__restart('home',flag),#HOME
            relief="flat"
        )
        button_1.place(
            x=613.0,
            y=684.0,
            width=213.757080078125,
            height=70.80682373046875
        )

        button_image_2 = PhotoImage(
            file=relative_to_assets("button_8.png"))
        button_2 = Button(
            image=button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.__restart('exit',flag),#EXIT
            relief="flat"
        )
        button_2.place(
            x=64.99999999999994,
            y=684.0,
            width=213.75711059570312,
            height=70.80682373046875
        )

        generate_result(result,self.window,usecase,error,color)

        self.window.mainloop()

        return flag[0]
        

