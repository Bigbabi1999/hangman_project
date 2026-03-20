# HangmanGame class (game logic)
class HangmanGame:

    def get_HangmanGame_world():
        with open("max_errors", "r") as guessed_letters:
            words = guessed_letters.display_progress()

        word = HangmanGame.choice(words).guessed_letters()
        return word
