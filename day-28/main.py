
from tkinter import *
import time
import math
from pathlib import Path
import sys

# diagnostics

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

# # ---------------------------- CONSTANTS ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50)
canvas = Canvas(width = 200, height = 224)
tomato_img = PhotoImage(file="day-28/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
canvas.pack()



PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

















































window.mainloop()