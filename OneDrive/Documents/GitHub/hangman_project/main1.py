from gameboard import Board
from ship import Ship
from player import Player, ComputerPlayer

from utils1 import log_game

# Setup
player = Player("You")
computer = ComputerPlayer("AI")
turns = 0

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
        log_game("Player", turns)
        break
    print("\nComputer's Turn")
    row, col = computer.get_shot(computer_board.size)
    result = player_board.take_shot(row, col, ships)
    print(result)

    if all(len(ship.coordinates) == 0 for ship in ships):
        print("Computer wins!")
        log_game("computer", turns)
        break