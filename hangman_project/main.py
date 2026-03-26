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

    result = game.process_guess(guess)

    if result:
        print("Correct guess!")
    else:
        print("Wrong guess!")

    game.display_process()

    # CHECK GAME END
    if game.is_won():
        print("You WON!")
        break

    if game.is_lost():
        print("You LOST!")
        print("the word was:", game.word)
        break
