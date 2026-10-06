# Renders the current time as three rows of ASCII seven-segment digits, with the date
# and weekday below, clearing and redrawing the terminal once per second.

import os
import time
from datetime import datetime

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

    time_str = now.strftime("%I:%M")
    sec_str = now.strftime("%S")
    ampm = now.strftime("%p")
    date_str = now.strftime("%B %d %Y").upper()
    day_str = now.strftime("%A").upper()

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

    GREEN = '\033[92m'
    RESET = '\033[0m'

    print(f"{GREEN}{row1}{RESET}")
    print(f"{GREEN}{row2}{RESET}")
    print(f"{GREEN}{row3}{RESET}")

    print()

    print(f"{GREEN}{date_str}      {day_str}{RESET}")

    time.sleep(1)