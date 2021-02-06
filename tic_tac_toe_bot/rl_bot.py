from tic_tac_toe import TicTacToe
from player import Player
from random import randint, random
from math import isclose
from copy import deepcopy
import pickle


class RLBot(Player):
    def __init__(self, marker: str, state_values: dict = {}):
        super().__init__(marker)
        self.state_values = state_values
        self.prev_state = None
    

    def get_legal_moves(self, game: TicTacToe):
        legal_moves = []
        board = game.get_board()
        for row in range(3):
            for col in range(3):
                if board[row][col] == "":
                    legal_moves.append((row, col))
        return legal_moves


    def get_possible_next_states(self, game: TicTacToe, legal_moves: list):
        planning_board = deepcopy(game.get_board())
        possible_states = []
        for move in legal_moves:
            planning_board[move[0]][move[1]] = self.marker
            state = TicTacToe.get_serialized_board(planning_board)
            possible_states.append(state)
            # reset planning board
            planning_board[move[0]][move[1]] = ""
        return possible_states


    def get_value(self, state: str):
        if state not in self.state_values:
            self.state_values[state] = .5
        return self.state_values[state]

    
    def choose_best_state_index(self, possible_states: list):
        state_values = []
        for state in possible_states:
            state_values.append(self.get_value(state))
        
        max_value = max(state_values)
        best_state_indices = []

        for i in range(len(possible_states)):
            if isclose(max_value, state_values[i]):
                best_state_indices.append(i)

        rand_index = randint(0, len(best_state_indices) - 1)
        best_state_index = best_state_indices[rand_index]
        return best_state_index, possible_states[best_state_index]

    
    def update_value(self, next_state, step_size=.25):
        if self.prev_state == None:
            return
        prev_state_value = self.get_value(self.prev_state)
        next_state_value = self.get_value(next_state)
        self.state_values[self.prev_state] = prev_state_value + \
            step_size*(next_state_value - prev_state_value)

    
    def update_end_position(self, outcome: int):
        winning_condition = TicTacToe.X_WINS
        if self.marker == 'o':
            winning_condition = TicTacToe.O_WINS
        if outcome == winning_condition:
            self.state_values[self.prev_state] = 1
        else:
            self.state_values[self.prev_state] = 0


    def play_move(self, game: TicTacToe, explore_frac = .1):
        explore_prob = random()
        explore = True if explore_prob <= explore_frac else False

        if explore:
            return self.play_exploratory_move(game)
        else:
            return self.play_greedy_move(game)

    

    def play_greedy_move(self, game: TicTacToe):
        legal_moves = self.get_legal_moves(game)
        possible_states = self.get_possible_next_states(game, legal_moves)

        best_state_index, best_state = self.choose_best_state_index(possible_states)
        # best_state_index is also best_move_index
        best_move = legal_moves[best_state_index]

        current_state = TicTacToe.get_serialized_board(game.get_board())
        outcome = game.update_board(best_move[0], best_move[1], self.marker)

        # Finished game outcomes are handled differently
        if outcome == TicTacToe.END_MOVE:
            self.update_value(best_state)

        self.prev_state = best_state
        return outcome


    def play_exploratory_move(self, game: TicTacToe):
        legal_moves = self.get_legal_moves(game)
        idx = randint(0, len(legal_moves) - 1)
        random_move = legal_moves[idx]

        outcome = game.update_board(random_move[0], random_move[1], self.marker)
        self.prev_state = TicTacToe.get_serialized_board(game.get_board())

        return outcome

    
def store_bot_data(bot: RLBot, filename="bot.pkl"):
    bot_data = {}
    bot_data["state_values"] = bot.state_values
    bot_data["marker"] = bot.marker
    pickle.dump(bot_data, open(filename, "wb"))

def load_bot_data(filename):
    return pickle.load(open(filename, "rb"))


