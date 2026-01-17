from tkinter import *
import random




BACKGROUND_COLOR = "#B1DDC6"

windows = Tk()
windows.title("Flashy")
windows.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height = 526, bg = BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file = "day-31\card_back.png")
canvas.create_image(400, 263, image = card_front_img)
canvas.grid(row=0, column=0, columnspan=2)
title_card = canvas.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
word_card = canvas.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

windows.mainloop()