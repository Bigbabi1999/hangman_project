# Helper functions
import random

def get_random():
    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    word = random.choice(words).strip()
    return word
