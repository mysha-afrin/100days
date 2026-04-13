from tkinter import *
import requests

def get_quote():
    url = "https://api.kanye.rest"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text = quote)
    return quote
    #Write your code here.



window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

print("done configuraing")

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="day-33/background.png")

print ("done loading images")

canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text= get_quote, width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="day-33\kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)



window.mainloop()
