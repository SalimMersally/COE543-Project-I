import json


from fileinput import filename
from traceback import format_tb
from function.costCalc import *
from function.treeEditDistance import *
from function.treePatch import *
from function.editScript import *
from pprint import pprint
import xml.etree.ElementTree as ET

from ctypes.wintypes import SIZE
import tkinter
from tkinter.filedialog import *
from tkinter import *

from turtle import color 
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets2")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def nextPage():
    getInputs()
    copyFiles()
    print(dictInputs)
    window.destroy()
    import page3
    
window = Tk()
window.title("Similarity Machine")
window.geometry("763x528")
window.configure(bg = "#FFFFFF")

fileA = ""
fileB = ""
dictInputs = {}
def choose_file(arg) :
    
    if arg == 1 :
        entry_3.delete(0, "end")
        fileA = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        entry_3.insert(0,fileA)
        #print("You have selected : %s" % fileA)
        #filepathA = filedialog.asksaveasfilename()
    if arg == 2 :
        entry_4.delete(0, "end")
        fileB = askopenfilename(filetypes = [('XML files', '*.xml'),('All files','*')])
        entry_4.insert(0,fileB)
        
def copyFiles():
    
    #save location A
    text_file = open("locA.txt", "w")
    n = text_file.write(entry_3.get())
    text_file.close()
    
    #save location B
    text_file = open("locB.txt", "w")
    n = text_file.write(entry_4.get())
    text_file.close()

    
def getInputs():
    dictInputs.update({'CostIns_Tag':entry_1.get(),
                       'CostDel_Tag':entry_2.get(),
                       'CostUpd_Tag':entry_5.get(),
                       'CostIns_attrib': entry_6.get(),
                       'CostDel_attrib': entry_7.get(),
                       'CostUpd_attrib': entry_8.get(),
                       'CostIns_Text':entry_9.get(),
                       'CostDel_Text':entry_10.get(),
                       'CostUpd_Text':entry_11.get()})
    with open('InputCosts.txt', 'w') as f:
        f.write(json.dumps(dictInputs))      
canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 528,
    width = 763,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    381.0,
    264.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    110.0,
    73.0,
    image=image_image_2
)

canvas.create_rectangle(
    89.0,
    158.0,
    318.0,
    450.0,
    fill="#174AFF",
    outline="")

canvas.create_text(
    110.0,
    175.0,
    anchor="nw",
    text="Choose your 1st file:",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_rectangle(
    360.0,
    105.0,
    675.0,
    450.0,
    fill="#AEC0FF",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    610.5,
    134.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_1.place(
    x=561.0,
    y=122.0,
    width=99.0,
    height=22.0
)
entry_1.config(justify="center")
canvas.create_text(
    372.0,
    126.0,
    anchor="nw",
    text="Cost of Inserting a Node:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=nextPage,
    relief="flat"
)
button_1.place(
    x=526.0,
    y=465.0,
    width=125.0,
    height=46.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose_file(1),
    relief="flat"
)
button_2.place(
    x=208.0,
    y=248.0,
    width=89.0,
    height=36.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: choose_file(2),
    relief="flat"
)
button_3.place(
    x=208.0,
    y=386.0,
    width=89.0,
    height=36.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    610.5,
    170.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_2.place(
    x=561.0,
    y=158.0,
    width=99.0,
    height=22.0
)
entry_2.config(justify="center")

canvas.create_rectangle(
    675.0,
    105.0,
    701.0,
    450.0,
    fill="#174AFF",
    outline="")

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    203.5,
    218.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_3.place(
    x=110.0,
    y=203.0,
    width=187.0,
    height=28.0
)

canvas.create_text(
    110.0,
    306.0,
    anchor="nw",
    text="Choose your 2nd file:",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    203.5,
    349.0,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_4.place(
    x=110.0,
    y=334.0,
    width=187.0,
    height=28.0
)

canvas.create_text(
    372.0,
    162.0,
    anchor="nw",
    text="Cost of Deleting a Node:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    610.5,
    206.0,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_5.place(
    x=561.0,
    y=194.0,
    width=99.0,
    height=22.0
)
entry_5.config(justify="center")

canvas.create_text(
    372.0,
    198.0,
    anchor="nw",
    text="Cost of Updating a Node:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    610.5,
    242.0,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_6.place(
    x=561.0,
    y=230.0,
    width=99.0,
    height=22.0
)
entry_6.config(justify="center")

canvas.create_text(
    372.0,
    234.0,
    anchor="nw",
    text="Cost of Inserting an Attribute:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    610.5,
    278.0,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_7.place(
    x=561.0,
    y=266.0,
    width=99.0,
    height=22.0
)
entry_7.config(justify="center")

canvas.create_text(
    372.0,
    270.0,
    anchor="nw",
    text="Cost of Deleting an Attribute:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    610.5,
    314.0,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_8.place(
    x=561.0,
    y=302.0,
    width=99.0,
    height=22.0
)
entry_8.config(justify="center")

canvas.create_text(
    372.0,
    306.0,
    anchor="nw",
    text="Cost of Updating an Attribute:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    610.5,
    350.0,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_9.place(
    x=561.0,
    y=338.0,
    width=99.0,
    height=22.0
)
entry_9.config(justify="center")

canvas.create_text(
    372.0,
    342.0,
    anchor="nw",
    text="Cost of Inserting a Text",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    610.5,
    386.0,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_10.place(
    x=561.0,
    y=374.0,
    width=99.0,
    height=22.0
)
entry_10.config(justify="center")

canvas.create_text(
    372.0,
    378.0,
    anchor="nw",
    text="Cost of Deleting a Text:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    610.5,
    422.0,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#FFFFFF",
    highlightthickness=0
)
entry_11.place(
    x=561.0,
    y=410.0,
    width=99.0,
    height=22.0
)
entry_11.config(justify="center")

canvas.create_text(
    372.0,
    414.0,
    anchor="nw",
    text="Cost of Updating a Text:",
    fill="#001B7C",
    font=("ArialMT", 14 * -1)
)

canvas.create_text(
    684.0,
    122.0,
    anchor="nw",
    text="I",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    140.0,
    anchor="nw",
    text="N",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    158.0,
    anchor="nw",
    text="P",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    176.0,
    anchor="nw",
    text="U",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    194.0,
    anchor="nw",
    text="T",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    225.0,
    anchor="nw",
    text="Y",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    243.0,
    anchor="nw",
    text="O",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    261.0,
    anchor="nw",
    text="U",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    279.0,
    anchor="nw",
    text="R",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    310.0,
    anchor="nw",
    text="C",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    328.0,
    anchor="nw",
    text="O",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    346.0,
    anchor="nw",
    text="S",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    364.0,
    anchor="nw",
    text="T",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)

canvas.create_text(
    681.0,
    382.0,
    anchor="nw",
    text="S",
    fill="#FFFFFF",
    font=("Arial BoldMT", 16 * -1)
)
window.resizable(False, False)
window.mainloop()
