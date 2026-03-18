# HangmanGame class (game logic)

import game 

def get_game_world():
    with open("wordlist.txt", "r") as file:
        words = file.readlines()

    word = game.choice(words).strip()
    return word
