from tic_tac_toe import TicTacToe
from random_bot import RandomBot


def play_game():
    game = TicTacToe()

    bot1 = RandomBot('o')

    bot2 = RandomBot('x')

    last_move = -1
    turn = 1

    while last_move != game.DRAW and last_move != game.X_WINS and last_move != game.O_WINS:
        if turn % 2 == 1:
            last_move = bot1.play_move(game)
        else:
            last_move = bot2.play_move(game)
        turn += 1
        game.print_board()
        


if __name__ == "__main__":
    play_game()
