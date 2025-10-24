
from tkinter import *
import time
import math
from pathlib import Path
import sys

# diagnostics

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#e9e4b0"

BUTTON_COLOR = "F7CAC9"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
title_label.grid(row=0, column=1)
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day-28/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
canvas.create_text(100, 130, text= "00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column=1)





# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 










button1 = Button(text = "Start", highlightthickness=0)
button1.grid(row=2, column=0)

button2 = Button(text = "Reset", highlightthickness=0)
button2.grid(row=2, column=2)

check_mark = Label(text = "✔️", fg = GREEN, bg = YELLOW)
check_mark.grid(row = 3, column =1)






























window.mainloop()