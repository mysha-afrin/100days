from tkinter import *

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(row = 1 , column=0, columnspan=2, pady = 20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic"))
        true_image = PhotoImage(file="day-34/true.png")
        false_image = PhotoImage(file="day-34/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0)
        self.false_button.grid(row=2, column=1)
        self.score_label = Label(text="Score: 0", bg = THEME_COLOR, fg= "white")
        self.score_label.grid(row=0, column=2)
        self.window.mainloop()