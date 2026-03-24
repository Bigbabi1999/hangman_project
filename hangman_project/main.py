# Game loop
class input():

    def get_input():
        with open("wordlist.txt", "r") as str:
            words = str.isalpha()

        word = input().choice(words).len()
        return word
