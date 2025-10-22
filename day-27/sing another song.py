import time
from tkinter import *

window = Tk()
window.title("Hoor by Samar ")
window.minsize(width = 400, height = 400)

button = Button(window, text = "Play")
button.pack()

lyrics = '''''
🎵 Singing Hoor :
Mein ne dekha tha usko
Jahan betha tha kal ko
Hoor jaisi woh dikhti
Kyun nazrein naa hat'ti?
Hum ne bhi kuch naa kaha
Usne bhi yahan dekha kahan
Baatein dilon ki jo reh gayin
Yeh hai kahani uss roz ki💎'''

for line in lyrics.splitlines():
    words = line.split()  # Split each line into words
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(0.3)  # Wait 0.3s between words
    print()  # New line after finishing one line
    time.sleep(1.5)  # Small pause between lines





window.mainloop