# tic_tac_toe.py : Handles tic tac toe game

class TicTacToe:

    def __init__(self):
        self.O_WINS = 0
        self.X_WINS = 1
        self.DRAW = 2
        self.END_MOVE = 3
        self.ILLEGAL_MOVE = 4

        self.board = self.create_board()

    def create_board(self):
        return [["", "", ""], ["", "", ""], ["", "", ""]]


    def get_board(self):
        return self.board


    def update_board(self, x, y, marker: str):
        if self._is_move_legal(x, y):
            self.board[x][y] = marker
        else:
            return self.ILLEGAL_MOVE
        if self.check_is_winner(marker):
            return self.O_WINS if marker == 'o' else self.X_WINS
        if self.check_board_full():
            return self.DRAW
        return self.END_MOVE


    def check_is_winner(self, marker: str):
        win_condition = str(marker * 3)
        # Check rows
        if "".join(self._get_row(0)) == win_condition \
            or "".join(self._get_row(1)) == win_condition \
            or "".join(self._get_row(2)) == win_condition:
            return True
        # Check columns
        elif "".join(self._get_column(0))  == win_condition \
            or "".join(self._get_column(1)) == win_condition \
            or "".join(self._get_column(2)) == win_condition:
            return True
        # Check Diagonals
        elif "".join(self._get_diagonal()) == win_condition \
            or "".join(self._get_diagonal(False)) == win_condition:
            return True

        else:
            return False


    def check_is_draw(self):
        if self.check_board_full():
            if not self.check_is_winner('o') and not self.check_is_winner('x'):
                return True
        return False 


    def print_board(self):
        print(self._get_printable_row(0))
        print("-+-+-")
        print(self._get_printable_row(1))
        print("-+-+-")
        print(self._get_printable_row(2))
        print()


    def check_board_full(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y] == "":
                    return False
        return True


    def _get_row(self, row: int):
        return self.board[row]


    def _get_column(self, column: int):
        return [self.board[0][column], self.board[1][column], self.board[2][column]]


    def _get_diagonal(self, upper_left: bool = True):
        if upper_left:
            return [self.board[0][0], self.board[1][1], self.board[2][2]]
        else:
            return [self.board[0][2], self.board[1][1], self.board[2][0]]


    def _is_move_legal(self, x: int, y: int):
        if self.check_is_winner("o") or self.check_is_winner("x"):
            return False
        return self.board[x][y] == ""


    def _get_printable_row(self, row: int):
        printable_row = ""
        for col in range(3):
            pos = self.board[row][col]
            if pos == "":
                printable_row += " "
            else:
                printable_row += pos
            if col != 2:
                printable_row += "|"
        return printable_row


    def get_serialized_board(self):
        empty_marker = "_"
        board_string = ""
        for row in range(3):
            for col in range(3):
                pos = self.board[row][col]
                if pos == "":
                    board_string += empty_marker
                else:
                    board_string += pos
        return board_string


def test():
    game = TicTacToe()
    game.print_board()
    game.update_board(0, 0, 'o')
    game.print_board()
    game.update_board(0, 1, 'x')
    game.print_board()
    game.update_board(1, 1, 'o')
    game.print_board()
    game.update_board(1, 2, 'x')
    game.print_board()
    game.update_board(2, 2, 'o')
    game.print_board()
    print(game.check_is_winner('o'))
    print(game.get_serialized_board())


if __name__ == "__main__":
    test()