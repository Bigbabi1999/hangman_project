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
