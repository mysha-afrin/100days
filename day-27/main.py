
from tkinter import *

window = Tk()
window.title("My First GUI Program")

window.minsize(width = 500, height = 300)
my_label = Label(window, text = "I am a Label")
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text = "New Text ")
my_label.grid(column = 0, row = 3)

def button_clicked():
    new_text = input.get()
    my_label.config(text = new_text)


button = Button(window, text = "click me", command=button_clicked)
#button.pack()
button.grid(column = 2 , row = 2)

input = Entry(width = 10)
input.grid(column= 2, row = 0)


entry = Entry(width = 30)
entry.insert(END, string = "Some text to begin with.")
entry.grid(column= 3, row = 4)

text = Text(height = 5, width= 30)
text.insert(END, "Example of multi-line text entry")
text.grid(column = 4, row = 5)

def spinbox_used():
    print(spinbox.get())
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column = 0, row =1)

def checkbutton_used():
    print(checked_state.get())
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checkbutton.grid(column=1, row=1)
def radio_used():
    print(radio_state.get())
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option 1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option 2", value=2, variable=radio_state, command = radio_used)
radiobutton1.grid(column=0, row=2)
radiobutton2.grid(column=1, row=2)

def listbox_used(event):
    print(listbox.get(listbox.curselection()))
listbox = Listbox(height=4)
fruits = ["Apple", "Banana", "Cherry", "Date"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=3, row=1)

window.mainloop()