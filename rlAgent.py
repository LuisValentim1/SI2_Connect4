import random
from move import Move
import pickle


class RLAgent:

    def __init__(self, filename, player_num):
        self.name = "RL Agent"
        self.reward = 0
        self.no_games = 0
        self.no_seq3 = 0
        self.file = filename
        self.epslon = 1
        self.learning_rate = 0.1
        self.moves = []
        self.player_num = player_num

    def play(self, board, move_dict):
        #define rewards for each play

        #reward him for playing
        self.reward += 1

        choice= None

        choice_rand = random.uniform(0, 1)
        if choice_rand < self.epslon:
           choice=random.randint(0, 6)
        else:
            choice = self.read_choice(board, move_dict)

        #needs to store its choice on a file with its weight (reward)

        return choice

    def seq3(self, no_seq3):
        #reward him for making a sequence of 3
        if no_seq3 > self.no_seq3:
            nseq3 = no_seq3 - self.no_seq3
            self.no_seq3 = no_seq3

            self.reward += 100*nseq3

    def wins(self, move_dict):
        #if the last move wins the game reward him
        self.reward += 10000

        self.reset(move_dict)

    def loses(self, move_dict):
        #if he loses reward him negatively
        self.reward -= 10000

        self.reset(move_dict)

    def read_choice(self, board, move_dict):
        choices = []
        for row in range(7):
            for col in range(6):
                if board[col * 7 + row].fill == 0:
                    new_board = [b.copy() for b in board]
                    new_board[col * 7 + row].fill = self.player_num
                    move = self.find_move_using_board(new_board, move_dict)
                    move.choice = row
                    choices.append(move)
                    break
        #read from file and choose the next move
        #depending on the weights stored for each possible decision (in this case 7)

        rewards = [c.reward for c in choices]
        max_value = max(rewards)
        index = rewards.index(max_value)
        return choices[index].choice

    def save_choice(self, move_dict):
        #store its choice on a file with its weight (reward)
        with open(self.file, 'wb') as f:
            pickle.dump(move_dict, f)
        return

    def add_move(self, board, move_dict):
        move = self.find_move_using_board(board, move_dict)
        # https://en.wikipedia.org/wiki/Q-learning
        move.reward += self.learning_rate * (self.reward - move.reward)
        self.moves.append(move)

    def find_move_using_board(self, board, move_dict: dict):
        _sum = Move.calc_sum_board(board)
        if _sum not in move_dict.keys():
            move_dict[_sum] = [Move([b.copy() for b in board], 0, -1)]
            return move_dict[_sum][0]
        else:
            for i, move in enumerate(move_dict[_sum]):
                if board == move.board_state:
                    move.reward += 1
                    return move
            move_dict[_sum] += [Move([b.copy() for b in board], 0, -1)]
            return move_dict[_sum][-1]

    def print_board(self,board):
        [print(b.fill,end=",") for b in board]

    def reset(self, move_dict):
        self.no_games += 1
        self.epslon *= 0.985
        self.moves[-1].reward += self.learning_rate * (self.reward - self.moves[-1].reward)
        print(self.moves)

        #store on file
        self.save_choice(move_dict)

        self.moves = []
        self.reward = 0
        self.no_seq3 = 0
