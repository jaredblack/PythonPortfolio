# Generates two chords to switch between in "One Minute Changes" exercise

import random

def generate():
    chords = ["A", "D", "E", "G", "C", "Am", "Em", "Dm", "A7", "D7",
            "E7", "G7", "C7", "B7", "F", "Fmaj7", "D/F#", "G/B", "C/G"]
    for i in range(100):
        chord1 = random.choice(chords)
        chord2 = random.choice(chords)
        print("Change " + str(i) + ": " + chord1 + " - " + chord2)

if __name__ == '__main__':
    generate()