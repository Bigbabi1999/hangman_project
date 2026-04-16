import random

class Player:
    def __init__(self, name):
        self.name = name
        self.shots_taken = set()

    def get_shot(self):
        while True:
            user_input = input("Enter coordinate (e.g., A1):").upper()

            try:
                col = ord(user_input[0]) - ord('A')
                row = int(user_input[1:]) - 1

                if (row, col) in self.shots_taken:
                    print("You already shot here!")
                    continue
                self.shots_taken.add((row, col))
                return row, col

            except:
                print("Invalid input! Try again")

class ComputerPlayer(Player):
    def get_shot(self, board_size):
        while True:
            row = random.randint(0, board_size - 1)
            col = random.randint(0, board_size - 1)
            if (row, col) not in self.shots_taken:
                self.shots_taken.add((row, col))
                print(f"Computer shoots at {chr(col + 65)}{row + 1}")
                return row, col