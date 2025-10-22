import time

def type_lyric(line, char_delay=0.065):
    """Prints each character of a line with a small delay for typewriter effect."""
    for char in line:
        print(char, end='', flush=True)
        time.sleep(char_delay)
    print()  # Move to next line

def print_lyrics():
    lyrics = [
        "Jodi Biroho Thake Amio Thaki",
        "Ke Bolo Shesh Hobe Age?",
        "Keno Je Eto Bhalobasha More Jay",
        "Shudhu Shonoy Mone Rakhe",
        "Eto Shunnota",
        "E Mone Rakhi Je Ami",
        "Dekhe Na Key To Ar",
        "Bole Eshob-I Paglami",
        "Kate Na Jamini",
        "Biroho Jeno Kete Jay",
        "Thame Na Borsha",
        "Tomare Daki Je Ami"
    ]

    # Delays in seconds for each line
    delays = [2.0, 1.8, 2.1, 2.4, 1.7, 2.0, 1.8, 2.1, 2.4, 1.7, 2.0, 1.8]

    print("\n\nNow Playing: Long Distance Love\n")
    time.sleep(1.5)

    for i, line in enumerate(lyrics):
        type_lyric(line)
        time.sleep(delays[i])

# Run the lyrics display
print_lyrics()
