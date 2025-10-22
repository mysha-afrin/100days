from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width = 500, height = 300)
my_label = Label(window, text = "I am a Label")
my_label.place(x = 100, y = 100)

my_label["text"] = "New Text"
my_label.config(text = "New Text ")
my_label.place(x = 150, y = 130)







window.mainloop()