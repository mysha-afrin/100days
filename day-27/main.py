
from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width = 500, height = 300)
my_label = Label(window, text = "I am a Label")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text ")


def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)


button = Button(window, text = "click me", command=button_clicked)
button.pack()


input = Entry(width = 10)
input.pack()
input.get()

entry = Entry(width = 30)
entry.insert(END, string = "Some text to begin with.")
entry.pack()

text = Text(height = 5, width= 30)
text.insert(END, "Example of multi-line text entry")
text.pack()
window.mainloop()