class Board:
    def __init__(self, size=5):
        self.size = size
        # Create a 2D grid filled with "~"
        self.grid = [["~" for _ in range(size)] for _ in range(size)]

    def print_board(self, hide_ships=True):
        # print column headers (A,B,C, ...)
        header = " " + " " .join(chr(ord('A') + i) for i in range(self.size))
        print(header)

        for i in range(self.size):
            row_display = []

            for cell in self.grid[i]:
                if hide_ships and cell == "S":
                    row_display.append("~") # hide ships
                else:
                    row_display.append(cell)

            # print row number + row content
            print(f"{i + 1}" + " ".join(row_display))

    def place_ship(self, row, col):
        self.grid[row][col] = "S"

    def mark_hit(self, row, col):
        self.grid[row][col] = "X"

    def mark_miss(self, row, col):
        self.grid[row][col] = "O"
