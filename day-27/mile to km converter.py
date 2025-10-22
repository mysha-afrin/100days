from tkinter import *
window = Tk()
window.title("Mile to km Converter")
window.minsize(width = 400, height = 200)
window.config(padx = 20 , pady = 20)

input_mile = Entry(width = 10)
input_mile.grid(column =4, row = 3)


def button_clicked():
    mile = float(input_mile.get())
    km = mile * 1.60934
    kilometer_result.config(text = f"{km}")


my_label = Label(text = "Miles")
my_label.grid(column= 5, row = 3)

my_label2 = Label(text = "is equal to")
my_label2.grid(column = 3, row = 5)


kilometer_result = Label(text = "0")
kilometer_result.grid(column = 4, row = 5)


my_label3 = Label(text = "km")
my_label3.grid(column = 5, row = 5)

button = Button(text = "Calculate", command = button_clicked)
button.grid(column = 4 , row = 6)





window.mainloop()