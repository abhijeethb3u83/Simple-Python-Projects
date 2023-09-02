import random


class Computer:
    """
    The computer.
    """

    def __init__(self, marker) -> None:
        self.marker = marker

    def get_move(self, game):
        """
        Method to obtain the computer move.
        Input: game board.
        """
        return random.choice(game.valid_moves()) - 1

    def get_name(self):
        """
        Returns computer name.
        """
        return "Computer"

    def get_marker(self):
        """
        Returns computer marker
        """
        return self.marker


class Human:
    """
    The human player.
    """

    def __init__(self, marker) -> None:
        self.marker = marker

    def get_move(self, game):
        """
        Method to obtain the players move.
        Input: game board.
        """
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
        """
        Returns player name.
        """
        return "Player"

    def get_marker(self):
        """
        Returns player marker
        """
        return self.marker
