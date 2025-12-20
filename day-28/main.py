
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
repr = 0
timer = None
window = Tk()
window.title("Pomodoro")
window.config(padx = 100, pady = 50, bg = YELLOW)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(repr/2)
        for _ in range(work_sessions):
            marks += "✔"
        check_marks.config(text=marks)

def start_countdown():
    global repr
    repr += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if repr % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)
    elif repr % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)

# 
#  

def say_something(message):
    print(message)

def start_timer():
    global repr
    repr += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if repr % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text = "Break", fg = RED)
        title_label.config(text = "✔️")
    elif repr % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text = "Break", fg = PINK)
    else:
        count_down(work_sec)
        title_label.config(text = "Work", fg = GREEN)
        title_label.config(text = "✔️")

"""def count_down(count):
    canvas.itemconfig(timer_text, text=f"{count // 60:02}:{count % 60:02}")
    if count > 0:
        window.after(1000, count_down, count - 1)
    else:
        start_timer()"""


window.after(2000, say_something, "Hello World!")  # Test after method


title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
title_label.grid(row=0, column=1)
canvas = Canvas(width = 200, height = 224, bg = YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="day-28/tomato.png")

canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text= "00:00", fill="white", font= (FONT_NAME, 35, "bold"))
canvas.grid(row = 1, column=1)





# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(count_down)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer")
    
# ---------------------------- TIMER MECHANISM ------------------------------- # 










button1 = Button(text = "Start", highlightthickness=0, command = start_countdown)
button1.grid(row=2, column=0)

button2 = Button(text = "Reset", highlightthickness=0, command= reset_timer)
button2.grid(row=2, column=2)

check_mark = Label(fg = GREEN, bg = YELLOW)
check_mark.grid(row = 3, column =1)


window.mainloop()