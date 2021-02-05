from tic_tac_toe import TicTacToe

class Player:
    def __init__(self, marker: str):
        self.marker = marker

    def play_move(self, game: TicTacToe, row: int, col: int):
        return game.update_board(row, col, self.marker)
        
