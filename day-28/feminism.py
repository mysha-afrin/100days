from tkinter import *
import time
import math
from pathlib import Path
import sys
import random
# diagnostics









# ---------------------------- UI SETUP ------------------------------- #

# # ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#e9e4b0"

BUTTON_COLOR = "#F7CAC9"
FONT_NAME = "Courier"
FONT_NAME2 = "Arial"
q_index = 0




question = ["Do you believe men and women should have equal rights?" ,

"Do you believe men and women deserve equal respect?",

"Should men and women have the same access to education?",

"Should women be able to work in any career they choose?",

'Should women receive equal pay for equal work?',

"Should promotions be based on ability, not gender?"

]

my_answer = [ "You are pure feminist! Pura 100%",
" You are a strong feminist! pura 75% 💪🌸",
" You are a moderate feminist! pura 50% 🌸",
"Feminist dektesi! 90%"





]

your_answer = random.choice(my_answer)







window = Tk()
window.title("feminism")
window.config(padx = 5, pady = 5, bg = YELLOW)



title_label = Label(text = "TEST IF YOU ARE FEMINIST.", font = (FONT_NAME, 50, "bold"), bg = YELLOW, fg = RED)
title_label.grid(column=2, row=1)
canvas = Canvas(width = 500, height = 450, bg = YELLOW, highlightthickness = 0)
canvas.grid(column=2 , row=2)
canvas_img = PhotoImage(file = "day-28\image.png")
canvas.create_image(236, 228, image = canvas_img)

def show_result(): 
    canvas.itemconfig(text_id, text=your_answer)
    '''button1.config(state="disabled") 
    button2.config(state="disabled")
    button3.config(state="disabled")'''
    button4 = Button(text="Restart", width=10, bg=BUTTON_COLOR, command=restart_test)
    button4.grid(column=2, row=4, pady=20)
    botton5 = Button(text="Exit", width=10, bg=BUTTON_COLOR, command=window.quit)
    botton5.grid(column=3, row=4, pady=20)
    button6 = Button(text="Close", width=10, bg=BUTTON_COLOR, command= window.destroy)
    button6.grid(column=1, row=4, pady=20) 
def next_question():
    global q_index
     
    q_index += 1 
    if q_index < len(question): 
        canvas.itemconfig(text_id, text=question[q_index])
        button1 = Button(text="Yes", width=10, bg=BUTTON_COLOR, command=on_yes)
        button1.grid(column=1, row=4, pady=20)
        button2 = Button(text="No", width=10, bg=BUTTON_COLOR, command=on_no)
        button2.grid(column=2, row=4, pady=20)
        button3 = Button(text="Skip", width=10, bg=BUTTON_COLOR, command=on_skip)
        button3.grid(column=3, row=4, pady=20)
 
    else: show_result()
def on_yes():
    canvas.itemconfig(text_id, text="You answered: Yes") 
    window.after(800, next_question) 
def on_no(): 
    canvas.itemconfig(text_id, text="You answered: No") 
    window.after(800, next_question)
def on_skip(): 
    canvas.itemconfig(text_id, text="Question skipped") 
    window.after(800, next_question) 
text_id = canvas.create_text( 320, 320)


def restart_test():
    global q_index
    q_index = 0
    canvas.itemconfig(text_id, text=question[q_index])
    button1 = Button(text="Yes", width=10, bg=BUTTON_COLOR, command=on_yes)
    button1.grid(column=1, row=4, pady=20)
    button2 = Button(text="No", width=10, bg=BUTTON_COLOR, command=on_no)
    button2.grid(column=2, row=4, pady=20)
    button3 = Button(text="Skip", width=10, bg=BUTTON_COLOR, command=on_skip)
    button3.grid(column=3, row=4, pady=20)


button1 = Button(text="Yes", width=10, bg=BUTTON_COLOR, command=on_yes)
button1.grid(column=1, row=4, pady=20)
button2 = Button(text="No", width=10, bg=BUTTON_COLOR, command=on_no)
button2.grid(column=2, row=4, pady=20)
button3 = Button(text="Skip", width=10, bg=BUTTON_COLOR, command=on_skip)
button3.grid(column=3, row=4, pady=20)


text_id = canvas.create_text(250, 50, width=400, text=question[0], font=(FONT_NAME2, 20, "bold"), fill=RED)






#qn_text = canvas.create_text(text = question[quen], font = (FONT_NAME2, 20, "bold"), bg = YELLOW, fg = RED, wraplength=400, justify="center")
#qn_text.grid(column=2, row=3)



window.mainloop()