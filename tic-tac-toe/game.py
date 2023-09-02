import player
import time


class TicTacToe:
    def __init__(self) -> None:
        self.board = [" "] * 9

    def print_board(self, show_pos=False):
        if show_pos:
            for row in [
                [str(i + 1) for i in range(j * 3, j * 3 + 3)] for j in range(3)
            ]:
                print(" | ".join(row))
        else:
            for row in [self.board[j * 3 : j * 3 + 3] for j in range(3)]:
                print(" | ".join(row))

    def valid_moves(self):
        moves = [idx + 1 for idx, spot in enumerate(self.board) if spot == " "]
        return moves

    def empty_squares(self):
        return " " in self.board

    def num_empty_squares(self):
        return self.board.count(" ")

    def mark_move(self, move: int, marker: str):
        self.board[move] = marker

    def check_winner(self, marker: str):
        for j in range(3):
            # 0 3 6 | 1 4 7 | 2 5 8
            if all([self.board[j + 3 * i] == marker for i in range(3)]):
                return True
            # 0 1 2 | 3 4 5 | 6 7 8
            if all([self.board[i + 3 * j] == marker for i in range(3)]):
                return True

        if all([self.board[i] == marker for i in [0, 4, 8]]):
            return True
        if all([self.board[i] == marker for i in [2, 4, 6]]):
            return True

        return False


def play(game: TicTacToe):
    # Select x and o players
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
        time.sleep(1)
        game.print_board()
        time.sleep(1)
        move_count += 1
        if move_count > 4:
            if game.check_winner(x_player.get_marker()):
                print(f"{x_player.get_name()} won!")
                return

        print(f"{o_player.get_name()}'s move")
        omove = o_player.get_move(game)
        game.mark_move(omove, o_player.get_marker())
        time.sleep(1)
        game.print_board()
        time.sleep(1)
        move_count += 1
        if move_count > 4:
            if game.check_winner(o_player.get_marker()):
                print(f"{o_player.get_name()} won!")
                return

    print("It's a draw :()")


if __name__ == "__main__":
    new_game = TicTacToe()
    play(new_game)