from tic_tac_toe import TicTacToe
from random_bot import RandomBot
from rl_bot import RLBot, store_bot_data, load_bot_data
from random import randint


def train(num_games: int = 100000, saved_bot_file = None):

    game_num = 0
    num_games_played = 0
    num_games_rl_bot_won = 0

    state_values = {}
    if saved_bot_file is None:
        rl_bot = RLBot('o')
    else:
        rl_bot_data = load_bot_data(saved_bot_file)
        rl_bot = RLBot(rl_bot_data["marker"], rl_bot_data["state_values"])

    
    
    while (game_num < num_games):

        game = TicTacToe()

        rl_bot_turn = randint(0, 1)

        if rl_bot.marker == 'o':
            random_bot = RandomBot('x')
        else:
            random_bot = RandomBot('o')


        last_outcome = -1
        turn = 1

        while last_outcome != TicTacToe.DRAW and last_outcome != TicTacToe.X_WINS and last_outcome != TicTacToe.O_WINS:
            if turn % 2 == rl_bot_turn:
                last_outcome = rl_bot.play_move(game)
            else:
                last_outcome = random_bot.play_move(game)
            turn += 1

        rl_bot.update_end_position(last_outcome)

        num_games_played += 1

        if last_outcome == TicTacToe.O_WINS:
            num_games_rl_bot_won += 1

        print("RL Bot Winning Percentage", num_games_rl_bot_won / num_games_played)
        #print(len(rl_bot.state_values))
        game_num += 1 

    #store_bot_data(rl_bot)


if __name__ == "__main__":
    train()