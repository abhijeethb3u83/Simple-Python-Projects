import player
import time
from typing import List


class TicTacToe:
    """
    The Tic Tac Toe game board.
    Depends on the player module for assigning players.
    """

    def __init__(self) -> None:
        self.board = [" "] * 9

    def print_board(self, show_pos=False):
        """
        Prints the board.
        If show_pos is set to True, it will print the positional coords
        of the board.
        """
        if show_pos:
            for row in [
                [str(i + 1) for i in range(j * 3, j * 3 + 3)] for j in range(3)
            ]:
                print(" | ".join(row))
        else:
            for row in [self.board[j * 3 : j * 3 + 3] for j in range(3)]:
                print(" | ".join(row))

    def valid_moves(self) -> List:
        """
        Returns a list of valid moves.
        """
        moves = [idx + 1 for idx, spot in enumerate(self.board) if spot == " "]
        return moves

    def empty_squares(self):
        """
        Find whether there are empty squares on board.
        Returns a boolean.
        """
        return " " in self.board

    def num_empty_squares(self):
        """
        Returns the number of empty squares.
        """
        return self.board.count(" ")

    def mark_move(self, move: int, marker: str):
        """
        Method to mark the players move on board
        """
        self.board[move] = marker

    def check_winner(self, square: int, marker: str):
        """
        Method which checks whether a player has won or not.
        Returns a boolean, True for success.
        """
        col = square % 3
        row = square // 3

        if all([self.board[slice(row*3,row*3+3)] == marker]):
            return True
        if all([self.board[slice(col,col+7, 3)] == marker]):
            return True
        
        if square % 2 == 0:
            if all([self.board[i] == marker] for i in [0,4,8]):
                return True
            if all([self.board[i] == marker] for i in [2,4,6]):
                return True


        return False


def play(game: TicTacToe):
    """
    The game mechanics
    Takes the gameboard as input
    """
    game.print_board(True)
    print()
    marker = input("Choose your marker! (X or O): ").capitalize()
    while marker not in ["X", "O"]:
        print("Wrong entry")
        marker = input("Choose your marker! (X or O): ").capitalize()

    x_player = player.Human("X") if marker == "X" else player.Computer("X")
    o_player = player.Human("O") if marker == "O" else player.Computer("O")

    move_count = 0
    while game.empty_squares():
        print(f"{x_player.get_name()}'s move")
        xmove = x_player.get_move(game)
        game.mark_move(xmove, x_player.get_marker())
        print(f"{x_player.get_name()}'s marks square {xmove+1}")
        time.sleep(1)
        game.print_board()
        time.sleep(1)
        move_count += 1
        if move_count > 4:
            if game.check_winner(xmove, x_player.get_marker()):
                print(f"\n{o_player.get_name()} : (｀□′)╯┴┴")
                print(f"{x_player.get_name()} wins!")
                return

        print(f"{o_player.get_name()}'s move")
        omove = o_player.get_move(game)
        game.mark_move(omove, o_player.get_marker())
        print(f"{o_player.get_name()}'s marks square {omove+1}")
        time.sleep(1)
        game.print_board()
        time.sleep(1)
        move_count += 1
        if move_count > 4:
            if game.check_winner(omove, o_player.get_marker()):
                print(f"\n{x_player.get_name()} : (｀□′)╯┴┴")
                print(f"{o_player.get_name()} wins!")
                return

    print("It's a draw :()")
