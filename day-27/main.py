
from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width = 500, height = 300)
my_label = Label(window, text = "I am a Label")
my_label.pack(side = "left")

my_label["text"] = "New Text"
my_label.config(text = "New Text 2")


def button_clicked():
    print("I got clicked")


button = Button(window, text = "click me", command=button_clicked)
button.pack(side = "right")








window.mainloop()