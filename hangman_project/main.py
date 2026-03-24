# Game loop
class main:

    def get_main_world():
        with open("wordlist.txt", "r") as str:
            words = str.isalpha()

        word = main.choice(words).len()
        return word
