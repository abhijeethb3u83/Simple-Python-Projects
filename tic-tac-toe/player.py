import random


class Computer:
    def __init__(self, marker) -> None:
        self.marker = marker

    def get_move(self, game):
        return random.choice(game.valid_moves()) - 1

    def get_name(self):
        return "Computer"

    def get_marker(self):
        return self.marker


class Human:
    def __init__(self, marker) -> None:
        self.marker = marker

    def get_move(self, game):
        your_move = -1
        available_moves = game.valid_moves()
        while your_move not in available_moves:
            try:
                your_move = int(input("Enter your move (1-9): "))
            except ValueError:
                print("Invalid move! Try again.")
            else:
                msg = (
                    "Move not available"
                    if your_move not in available_moves
                    else "Good move"
                )
                print(msg)
        return your_move - 1

    def get_name(self):
        return "Player"

    def get_marker(self):
        return self.marker
