from tkinter import Canvas, Entry, Tk, PhotoImage, Label, Button
import random

BACKGROUND_COLOR = "#E8E4C9"
FONT_NAME = "Arial"

windows = Tk()
windows.title("Password Manager")
windows.config(padx= 20, pady= 20, bg = BACKGROUND_COLOR , highlightthickness = 0)



def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    with open("day-29/data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")

















logo_image = PhotoImage(file="day-29/logo.png")
canvas = Canvas(width = 200, height = 200, bg = BACKGROUND_COLOR, highlightthickness = 0)
canvas.create_image(100, 100, image = logo_image)
canvas.grid(column=2, row=2)

my_label = Label(text= "website:", bg= BACKGROUND_COLOR, font=(FONT_NAME, 12, "bold"))
my_label.grid(column=1, row=3)

website_entry = Entry(width=35)
website_entry.grid(column=2, row=3, columnspan=2)

my_label = Label(text= "email/username:", bg= BACKGROUND_COLOR, font=(FONT_NAME, 12, "bold"))
my_label.grid(column=1, row=4)

email_entry = Entry(width=35)
email_entry.grid(column=2, row=4, columnspan=2)
email_entry.insert(0, "myshaafrinjeba916@gamil.com")

my_label = Label(text= "password:", bg= BACKGROUND_COLOR, font=(FONT_NAME, 12, "bold"))
my_label.grid(column=1, row=5)

password_entry = Entry(width = 21)
password_entry.grid(column=2, row=5, columnspan=1)


Generate_password_button = Button(text= "Generate Password", width = 14)
Generate_password_button.grid(column=3, row=5, columnspan=1)

add_button = Button(text= "Add", width = 36)
add_button.grid(column=2, row=6, columnspan=2, command= save_password)





windows.mainloop()