
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
WORK_MIN = 2
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 2
reps = 0
timer = None
check_marks = ""


windows = Tk()
windows.title("Pomodoro")
windows.config(padx = 100, pady = 50, bg = YELLOW)
windows.minsize(width = 400, height = 300)

title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
title_label.grid(column = 2, row =1)

canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness = 0)
canvas.grid(column=2, row=2)
tomato_img = PhotoImage(file = Path(sys.path[0]) / "tomato.png")
canvas.create_image(100, 112, image = tomato_img)
# ---------------------------- TIMER MECHANISM ------------------------------- #





# ---------------------------- TIMER RESET ------------------------------- #























#---------------------------- BUTTONS -------------------------------- #

start_button = Button(text = "Start", highlightthickness=0, command = None)
start_button.grid(column=1, row=3)
reset_button = Button(text = "Reset", highlightthickness=0, command= None)
reset_button.grid(column = 3 , row= 3)




windows.mainloop()