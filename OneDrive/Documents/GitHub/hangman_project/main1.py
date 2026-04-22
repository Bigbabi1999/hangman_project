from gameboard import Board
from ship import Ship
from player import Player, ComputerPlayer
from utils1 import log_game

def play_game():
    # Setup
    player = Player("You")
    computer = ComputerPlayer("AI")
    turns = 0
    ships_sunk = 0

    player_board = Board()
    computer_board = Board()

    # Create ships
    ships = [Ship("Destroyer", 2), Ship("Submarine", 3)]
    # Place ships
    for ship in ships:
        player_board.place_ship(ship)

    computer_ships = [Ship("Destroyer", 2), Ship("Submarine", 3)]
    for ship in computer_ships:
        computer_board.place_ship(ship)

    # Game loop
    while True:
        turns += 1
        print("\nYour Turn")
        computer_board.print_board()

        row, col = player.get_shot()
        result = computer_board.take_shot(row, col, computer_ships)
        print(result)


        # Check win
        if all(len(ship.coordinatescoordinates) == 0 for ship in computer_ships):
            print("You win!")
            log_game("Player", turns, ships_sunk)
            break

        print("\nComputer's Turn")
        row, col = computer.get_shot(computer_board.size)
        result = player_board.take_shot(row, col, ships)
        print(result)

        #Track ships sunk by computer
        if "sunk" in result.lower():
            ships_sunk += 1

        if all(len(ship.coordinates) == 0 for ship in ships):
            print("Computer wins!")
            log_game("computer", turns)
            break

def view_history():
    try:
        with open("battle_log.txt", "r") as file:
            print("\n=== GAME HISTORY===")
            print(file.read())
    except FileNotFoundError:
        print("No game history found")

def main():
    while True:
        print("\n=== BATTLESHIP MENU ===")
        print("1. Play Game")
        print("2. View Game History")
        print("3. Exit")

        choice = input("Enter your choice:")
        if choice == "1":
                play_game()

        elif choice == "2":
            view_history()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("invalid choice, try again")

if __name__ == "__main__":
        main()
