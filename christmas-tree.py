import time
import os
import random

colors = [
    "\033[91m", "\033[92m", "\033[93m",
    "\033[94m", "\033[95m", "\033[96m"
]
reset = "\033[0m"

tree_template = [
    "         *",
    "        ***",
    "       *****",
    "      *******",
    "     *********",
    "    ***********",
    "        |||",
]

def colourize_lights(line):
    result = ""
    for c in line:
        if c == "*":
            result += random.choice(colors) + "*" + reset
        else:
            result += c
    return result


lyrics_timed = [
    ( 0, "🎶 Last Christmas, I gave you my heart"),
    ( 3, "But the very next day you gave it away"),
    ( 7, "This year, to save me from tears"),
    (10, "I'll give it to someone special"),

    (82, "Last Christmas, I gave you my heart"),
    (87, "But the very next day you gave it away"),
    (93, "This year, to save me from tears"),
    (98, "I'll give it to someone special 🎶"),
]

def main():
    start = time.time()
    next_line = 0
    current_lyric = ""

    while True:
        os.system("cls" if os.name == "nt" else "clear")

        print("\n")
        for line in tree_template:
            print(colourize_lights(line))

        now = time.time() - start
        if next_line < len(lyrics_timed) and now >= lyrics_timed[next_line][0]:
            current_lyric = lyrics_timed[next_line][1]
            next_line += 1

        print("\n  ► " + current_lyric)

        time.sleep(0.5)


if __name__ == "__main__":
    main()
