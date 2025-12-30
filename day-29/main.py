from tkinter import Canvas, Tk, PhotoImage, Label, Button
import random

BACKGROUND_COLOR = "#E8E4C9"
FONT_NAME = "Arial"

windows = Tk()
windows.title("Password Manager")
windows.config(padx= 20, pady= 20, bg = BACKGROUND_COLOR , highlightthickness = 0)

logo_image = PhotoImage(file="day-29/logo.png")
canvas = Canvas(width = 200, height = 200, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=2, row=2)


















windows.mainloop()