import tkinter


window = tkinter.Tk()
window.title("My First GUI Program")

window.minsize(width = 500, height = 300)
my_lebel = tkinter.Label(text = "I am a Label")
my_lebel.pack(side = "left")


window.mainloop()