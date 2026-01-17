from tkinter import *
import random
import pandas

data = pandas.read_csv("day-31\\french_words.csv")
to_learn = data.to_dict(orient = "records")
current_card = {}
#------------------------------Brain of the flash card app----------------#
def next_card():
    global current_card, flip_timer
    windows.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_card, text="French", fill = "black")
    canvas.itemconfig(word_card, text=current_card["French"], fill = "black")
    canvas.itemconfig(card_background, image=card_front_img)
    windows.after(3000, func= flip_card)
def flip_card():
    current_card = random.choice(to_learn)
    canvas.itemconfig(title_card, text = "English", fill = "white")
    canvas.itemconfig(word_card, text = current_card["English"], fill = "white")
    canvas.itemconfig(card_background, image = card_back_img)
#----------------------------Constants---------------#
BACKGROUND_COLOR = "#B1DDC6"


#------------------------------UI Setup
windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = windows.after(3000, func= flip_card)
canvas = Canvas(width=800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file = "day-31\card_front.png")
card_back_img = PhotoImage(file = "day-31\card_back.png")
card_background =canvas.create_image(400, 263, image = card_front_img)

canvas.grid(row=0, column=0, columnspan=2)
title_card = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

cross_image = PhotoImage(file="day-31\wrong.png")

wrong_button = Button(image = cross_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

check_image = PhotoImage(file= "day-31\\right.png")

right_button = Button(image = check_image, highlightthickness=0, command=next_card)
right_button.grid(row=1, column=0)
next_card()

windows.mainloop()