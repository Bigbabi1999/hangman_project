# Game loop
from game import HangmanGame
from utils import get_random_word

word = get_random_word()
game = HangmanGame(word)

while True:
    guess = input("Enter a letter: ").lower()

    # check: single letter
    if len(guess) != 1:
        print("Please enter ONLY one letter")
        continue
              
    # check: must be alphabet
    if not guess.isalpha():
        print("please enter a LETTER")
        continue

    # check: already guessed
    if guess in game.guessed_letters:
        print("you already guessed that letter")
        continue

    # valid input
    game.guessed_letters.append(guess)
    break
