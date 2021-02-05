from tic_tac_toe import TicTacToe
from player import Player
from random import randint

class RandomBot(Player):
    def __init__(self, marker: str):
        super().__init__(marker)

    def get_legal_moves(self, game: TicTacToe):
        legal_moves = []
        board = game.get_board()
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    legal_moves.append((row, col))
        return legal_moves


    def play_move(self, game: TicTacToe):
        legal_moves = self.get_legal_moves(game)
        idx = randint(0, len(legal_moves) - 1)
        random_move = legal_moves[idx]
        return game.update_board(random_move[0], random_move[1], self.marker)
        
