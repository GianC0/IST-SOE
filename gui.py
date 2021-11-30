from pathlib import Path
from PIL import ImageTk, Image
from tkinter import Label, Tk, Canvas, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)

class GUI():
    def __init__(self):
        pass
    
    def show(self):
        window = Tk()
        window.geometry("1440x780")
        window.configure(bg = "#FFFFFF")

        bg = ImageTk.PhotoImage(Image.open(
            'C:/Users/Matteo/Desktop/Lione/SOE/finalProject/Application/build/assets/back.jpg').resize((1440, 780)))

        canvas = Canvas(
            window,
            bg = "#FFFFFF",
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
            command=lambda: print("button_1 clicked"),
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
            command=lambda: print("button_2 clicked"),
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
            command=lambda: print("button_3 clicked"),
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
            command=lambda: print("button_4 clicked"),
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
        window.resizable(False, False)
        window.mainloop()
        return

gui = GUI()
gui.show()