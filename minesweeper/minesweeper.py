# Minesweeper game on the terminal
"""
Steps involved
Step 1:
Create the board and place the bombs
Step 2:
Show the user the board
Step 3:
Ask the user for coords of the location they want to dig
Step 4:
If the location has bomb end game.
Else recursively find all the nearyby bombs
Step 5:
Repeat 2 to 4 until the game is over.
"""
import random
import time


class Field:
    def __init__(self, size, bombs) -> None:
        self.size = size

        self.bombs = bombs

        self.field = self.create_field()

        self.place_markers()

        self.flags = set()
        # remember the positions of the already dug cells
        self.dug = set()

    def create_field(self):
        """
        Create the mine field
        """
        field = [[None for _ in range(self.size)] for _ in range(self.size)]

        bombs_planted = 0

        while bombs_planted < self.bombs:
            # get the location
            loc = random.randint(0, self.bombs**2 - 1)
            # get row and col indexes
            row = loc // self.size
            col = loc % self.size

            # check if a bomb is already present
            if field[row][col] == "*":
                continue

            # plant the bomb
            field[row][col] = "*"  # type: ignore
            bombs_planted += 1  # increment the coutner

        return field

    def place_markers(self):
        """
        Places the bombs on the field
        """
        # maximum number of bombs surrounding a cell = 8
        # so markers can vary from 0 to 8

        for r in range(self.size):
            for c in range(self.size):
                if self.field[r][c] == "*":
                    continue
                self.field[r][c] = self.get_num_neighbouring_bombs(r, c)  # type: ignore

    def get_num_neighbouring_bombs(self, row, col):
        """
        Returns number of neighbouring bombs
        """
        num_neighbouring_bombs = 0

        #              r-1,c
        #    r, c-1    r, c     r, c+1
        #              r+1, c

        for r in range(max(row - 1, 0), min(row + 1, self.size)):
            for c in range(max(col - 1, 0), min(col + 1, self.size)):
                if r == row and c == col:
                    continue
                print(r, c)
                if self.field[r][c] == "*":
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def dig(self, row, col):
        """
        Dig the field for bombs
        """
        # should recursively dig the positions until it finds cells with bombs
        # and keep adding the already dug cells into self.dug
        self.dug.add((row, col))
        print(row, col)
        if self.field[row][col] == "*":
            return False
        elif self.field[row][col] > 0:
            return True

        for r in range(max(row - 1, 0), min(row + 1, self.size)):
            for c in range(max(col - 1, 0), min(col + 1, self.size)):
                if (r, c) in self.dug:
                    continue
                self.dig(r, c)
        return True

    def __str__(self):
        visible_board = [[None for _ in range(self.size)] for _ in range(self.size)]
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) in self.dug:
                    visible_board[row][col] = str(self.field[row][col])  # type: ignore
                else:
                    visible_board[row][col] = " "  # type: ignore
        for row, col in self.flags:
            if (row, col) not in self.dug:
                visible_board[row][col] = "F"

        res = ""
        res += " " + " | " + " | ".join([str(i) for i in range(10)]) + " | " + "\n"
        res += "-" * 43 + "\n"
        for idx, row in enumerate(visible_board):
            res += (
                str(idx)
                + " | "
                + " | ".join([str(i) if i is not None else " " for i in row])
                + " | "
                + "\n"
            )
        res += "-" * 43 + "\n"

        return res


def play(size=10, bombs=10):
    if size < 10 or bombs < 10:
        size = 10
        bombs = 10
    # create the field
    field = Field(size, bombs)
    print("""
        Instructions:
        Enter the row, col (0-9) when prompted.
        Additionally enter the flag 'f' to place a marker
          flag on the field.
          """)
    not_bomb = True
    while len(field.dug) < size**2 - bombs:
        print(field)
        time.sleep(2)
        user_input = input("Where would you like to dig? Input as row,col: ").split()
        if len(user_input) > 3:
            print("Wrong input, enter again")
            continue
        row, col = int(user_input[0].strip()), int(user_input[1].strip())
        if len(user_input) == 3:
            if user_input[2].strip().lower() == "f":
                field.flags.add((row, col))
                continue

        if not (0 <= row < size) or not (0 <= col < size):
            print("Invalid location. Try again.")
            continue

        not_bomb = field.dig(row, col)
        if not not_bomb:
            # found a bomb
            break
    print("")
    if not_bomb:
        print("Lets see the final results... dum dum tsssss")
        time.sleep(2)
        print("CONGRATULATIONS!!!! YOU ARE VICTORIOUS!")
    else:
        print("SORRY GAME OVER :(")
        # let's reveal the whole board!
        field.dug = set((r, c) for r in range(size) for c in range(size))
        print(field)
        print("Better Luck next time!!!!!")
        time.sleep(2)


if __name__ == "__main__":
    play()
