import time
from tkinter import *
import threading  # To avoid freezing the GUI

# Create window
window = Tk()
window.title("Hoor by Samar")
window.minsize(width=500, height=400)
window.configure(bg="#111")

# Text box to display lyrics
text_box = Text(window, wrap="word", font=("Consolas", 14), bg="#222", fg="#00ff99")
text_box.pack(padx=20, pady=20, fill="both", expand=True)
text_box.config(state="disabled")  # Make it read-only

# Lyrics
lyrics = '''🎵 Singing Hoor :
Mein ne dekha tha usko
Jahan betha tha kal ko
Hoor jaisi woh dikhti
Kyun nazrein naa hat'ti?
Hum ne bhi kuch naa kaha
Usne bhi yahan dekha kahan
Baatein dilon ki jo reh gayin
Yeh hai kahani uss roz ki💎'''

# Function to play lyrics word by word
def play_lyrics():
    def animate():
        text_box.config(state="normal")
        text_box.delete("1.0", END)  # Clear previous text
        for line in lyrics.splitlines():
            words = line.split()
            for word in words:
                text_box.insert(END, word + ' ')
                text_box.see(END)  # Auto-scroll
                text_box.update_idletasks()
                time.sleep(0.3)  # Word delay
            text_box.insert(END, '\n')  # New line after each line
            time.sleep(0.5)  # Line delay
        text_box.config(state="disabled")
    
    # Run in a separate thread so GUI doesn't freeze
    threading.Thread(target=animate, daemon=True).start()

# Button to play lyrics
button = Button(window, text="▶ Play", font=("Arial", 14, "bold"),
                bg="#00ccff", fg="white", command=play_lyrics)
button.pack(pady=10)

window.mainloop()
