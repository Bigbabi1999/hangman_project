# Game loop
import main

def get_main_world():
    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    word = main.choice(words).strip()
    return word
