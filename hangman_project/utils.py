# Helper functions
import random

def get_random_world():
    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    word = random.choice(words).strip()
    return word