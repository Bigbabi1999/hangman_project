# HangmanGame class (game logic)
import HangmanGame

def get_HangmanGame_world():
    with open("wordlist.txt", "r") as guessed_letters:
        words = guessed_letters.readlines()

    word = HangmanGame.choice(words).strip()
    return word
