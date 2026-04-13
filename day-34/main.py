from tkinter import *
import requests

THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzler app")
window.minsize(width=500, height =500)
window.config(padx=20, pady=20, bg= THEME_COLOR)


canvas = Canvas(width=300, height=250,bg = "white", highlightthickness=0)
canvas.grid(row=2, column = 1, columnspan=4, pady=50)
false_image = PhotoImage(file= "day-34/false.png")
true_image = PhotoImage(file= "day-34/true.png")

#------------------------------Buttons----------------#
false_button = Button(image = false_image, highlightthickness=0)
false_button.grid(row=3, column = 4)

true_button = Button(image = true_image, highlightthickness=0)
true_button.grid(row=3, column = 0)













window.mainloop()