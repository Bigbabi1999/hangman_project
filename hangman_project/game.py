# HangmanGame class (game logic)
class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.max_errors = 6
        self.errors = 0

    def display_progress(self):
        result = ""

        for letter in self.word:
            if letter in self.guessed_letters:
                result += letter + " "
            else:
                result += "_"

        return result.strip()

    def process_guess(self, letter):
        # check if letter is in the word
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True
        else:
            self.errors += 1
            return False

    def display_process(self):
        display = ""

        for letter in self.word:
            if not letter.isalpha():
                display += letter + " "
            elif letter in self.guessed_letters:
                display += letter + " "
            else:
                display += "_"

        print(display.strip())

    def is_won(self):
        for letter in self.word:
            if letter not in self.guessed_letters:
                return False
        return True

    def is_lost(self):
        return self.errors >= self.max_errors

    str.isalpha()
    display_progress()
    # dont make it manuelly-reveal make it automactically-reveal and dont make it to far
