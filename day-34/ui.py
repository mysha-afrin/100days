from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.canvas.grid(row = 1 , column=0, columnspan=2, pady = 20)
        self.question_text = self.canvas.create_text(150, 125, width=280, text="Some Question Text", fill=THEME_COLOR, font=("Arial", 20, "italic") )
        true_image = PhotoImage(file="day-34/true.png")
        false_image = PhotoImage(file="day-34/false.png")
        self.true_button = Button(image=true_image, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(row=2, column=0)
        self.false_button = Button(image=false_image, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(row=2, column=1)
        self.score_label = Label(text="Score: 0", bg = THEME_COLOR, fg= "white")
        self.score_label.grid(row=0, column=2)
        self.get_next_question()
        self.window.mainloop()


    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text = q_text)
        self.score_label.config(text=f"Score: {self.quiz.score}")

    def true_pressed(self):
        self.quiz.check_answer("True")
        self.get_next_question()

    def false_pressed(self):
        self.quiz.check_answer("False")
        self.get_next_question()

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)