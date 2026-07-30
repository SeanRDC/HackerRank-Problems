# HOW TO RUN THIS CODE:
# 1. Save this entire script as a Python file
# 2. Open computer's Terminal or Command Prompt
# 3. Use the 'cd' command to navigate to the folder
# 4. Type: python clock.py (or python3 clock.py on Mac/Linux) and press Enter!
# 5. To stop exit the clock, press: Ctrl + C
# MADE BY:
# Sean Rhani Dela Cruz, CS - 302

import os
import time
from datetime import datetime

# THE ASCII ART DICTIONARY
DIGITS = {
    '0': [" _ ", "| |", "|_|"],
    '1': ["   ", "  |", "  |"],
    '2': [" _ ", " _|", "|_ "],
    '3': [" _ ", " _|", " _|"],
    '4': ["   ", "|_|", "  |"],
    '5': [" _ ", "|_ ", " _|"],
    '6': [" _ ", "|_ ", "|_|"],
    '7': [" _ ", "  |", "  |"],
    '8': [" _ ", "|_|", "|_|"],
    '9': [" _ ", "|_|", " _|"],
    ':': ["   ", " o ", " o "],
    ' ': ["   ", "   ", "   "]
}

while True:
    now = datetime.now()
    os.system('cls' if os.name == 'nt' else 'clear')

    # PARSING THE TIME & DATE

    time_str = now.strftime("%I:%M")
    sec_str = now.strftime("%S")
    ampm = now.strftime("%p")
    date_str = now.strftime("%B %d %Y").upper()
    day_str = now.strftime("%A").upper()

    # BUILDING THE ASCII CLOCK

    row1 = ""
    row2 = ""
    row3 = ""

    for char in time_str:
        art = DIGITS[char]
        row1 += art[0] + " "
        row2 += art[1] + " "
        row3 += art[2] + " "

    row1 += f" {ampm}"
    row3 += f" {sec_str}"


    # COLORING AND ASSEMBLY

    GREEN = '\033[92m'
    RESET = '\033[0m'

    print(f"{GREEN}{row1}{RESET}")
    print(f"{GREEN}{row2}{RESET}")
    print(f"{GREEN}{row3}{RESET}")

    print()

    print(f"{GREEN}{date_str}      {day_str}{RESET}")

    time.sleep(1)