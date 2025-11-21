from tkinter import *
import time
import math
from pathlib import Path
import sys

# diagnostics









# ---------------------------- UI SETUP ------------------------------- #

# # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#e9e4b0"

BUTTON_COLOR = "#F7CAC9"
FONT_NAME = "Courier"

window = Tk()
window.title("feminism")
window.config(padx = 10, pady = 5, bg = YELLOW)

title_label = Label(text = "FEMINISM", font = (FONT_NAME, 50, "bold"), bg = YELLOW, fg = RED)
title_label.grid(column=2, row=1)
canvas = Canvas(width = 500, height = 450, bg = GREEN, highlightthickness = 0)
canvas.grid(column=2 , row=2)
canvas_img = PhotoImage(file = "day-28\\feminism.png")
canvas.create_image(236, 225, image = canvas_img)





window.mainloop()