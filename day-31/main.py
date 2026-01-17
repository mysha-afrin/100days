from tkinter import *
import random
import pandas

data = pandas.read_csv("day-31\\french_words.csv")
print(data)
#------------------------------Brain of the flash card app----------------#
def next_card():
    pass

#----------------------------Constants---------------#
BACKGROUND_COLOR = "#B1DDC6"


#------------------------------UI Setup
windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file = "day-31\card_back.png")
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
title_card = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

cross_image = PhotoImage(file="day-31\wrong.png")

wrong_button = Button(image = cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

check_image = PhotoImage(file= "day-31\\right.png")

right_button = Button(image = check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)

windows.mainloop()