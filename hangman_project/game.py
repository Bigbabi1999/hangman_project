# HangmanGame class (game logic)
import HangmanGame

def get_HangmanGame_world():
    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    word = HangmanGame.choice(words).strip()
    return word
