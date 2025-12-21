
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


timer_text = canvas.create_text(100, 130, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))

check_marks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 20, "bold"))
check_marks.grid(column = 2, row = 4)
# ---------------------------- TIMER MECHANISM ------------------------------- #

def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = windows.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text = marks)
        check_marks.grid(column=2, row=4)
        







def start_timer():
    global reps
    reps += 1 
    work_min = WORK_MIN * 60
    short_break_min = SHORT_BREAK_MIN * 60
    long_break_min = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_min)
        title_label.config(text = "Break", fg = RED)
    elif reps % 2 == 0:
        count_down(short_break_min)
        title_label.config(text = "Break", fg = PINK)
    else:
        count_down(work_min)
        title_label.config(text = "Work", fg = GREEN)





# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps, timer
    if timer:
        windows.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer", fg = GREEN)
    reps = 0
    check_marks.config(text = "")





















#---------------------------- BUTTONS -------------------------------- #

start_button = Button(text = "Start", highlightthickness=0, command = start_timer)
start_button.grid(column=1, row=3)
reset_button = Button(text = "Reset", highlightthickness=0, command= reset_timer)
reset_button.grid(column = 3 , row= 3)




windows.mainloop()