from tkinter import Canvas, Entry, Tk, PhotoImage, Label, Button, messagebox
import random

BACKGROUND_COLOR = "#F0EFEB"
FONT_NAME = "Arial"
LETTERS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!#$%&()*+'
BUTTON_COLOR = "#B0DBF3"

def save_password():
    with open("data.txt", "a") as data_file:
        website = website_entry.get()
        email = email_entry.get()
        password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title = "Error", message = "Please don't leave any fild empty!")
        print("Please fill in all fields")
    
    if len(password) < 8 :
        messagebox.showinfo(title = "Error", message = "Password must be at least 8 characters long!")
        return
    if not any(char.isdigit() for char in password):
        messagebox.showinfo(title = "Error", message = "Password must contain at least one number!")
        return
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                            f"\nPassword: {password} \nIs it ok to save?")

    if is_ok:

        with open("day-29/data.txt", "a") as data_file:
            data_file.write(f"{website} / {email} / {password}\n")
            website_entry.delete(0, 'end')
            email_entry.delete(0, 'end')
            password_entry.delete(0, 'end')
            messagebox.showinfo(title="Passord Manager", message="Password saved successfully!")


def generate_password():
    password = []
    for _ in range(4):
        password.append(random.choice(LETTERS))
    for _ in range(4):
        password.append(random.choice(NUMBERS))
    for _ in range(2):
        password.append(random.choice(SYMBOLS))
    random.shuffle(password)
    password_entry.delete(0, 'end')
    password_entry.insert(0, ''.join(password))


windows = Tk()
windows.title("Password Manager")
windows.config(padx= 20, pady= 20, bg = BACKGROUND_COLOR , highlightthickness = 0)



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

password_entry = Entry(width = 35)
password_entry.grid(column=2, row=5, columnspan=1)
password_entry["width"] = 10

Generate_password_button = Button(text= "Generate Password", width = 14, command = generate_password)
Generate_password_button.grid(column=3, row=5, columnspan=1)

add_button = Button(text= "Add", width = 36, bg = BUTTON_COLOR, command= save_password)
add_button.grid(column=2, row=6, columnspan=2)





windows.mainloop()