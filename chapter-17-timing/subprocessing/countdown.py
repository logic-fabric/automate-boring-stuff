"""Script to lanuch a countdown from COUNTDOWN_START to zero before playing a sound.
"""

import subprocess
import time


COUNTDOWN_START = 5
SOUND_FILE = 'beretta.mp3'


def display_countdown(start=COUNTDOWN_START):
    for n in range(start, 0, -1):
        print(f"{n}...")
        time.sleep(1)

def play_sound(sound_file=SOUND_FILE):
    subprocess.Popen(['open', sound_file])


if __name__ == '__main__':
    display_countdown()
    print("FIRE!!!")
    play_sound()
