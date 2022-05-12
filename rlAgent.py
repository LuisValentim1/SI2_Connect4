import random

class RLAgent:

    def __init__(self):
        self.name = "RL Agent"
        self.reward = 0
        self.no_games = 0

    def play(self):
        #define rewards for each play

        #reward him for playing
        self.reward += 1 

        #read
        choice= None

        if self.no_games<100:
            choice=random.randint(0, 6)
        else:
            #read from file and choose the next move
            #depending on the weights stored for each possible decision (in this case 7)
            None #change None with code for reading the file

        #confirm final reward for the choice
        #
        #

        #needs to store its choice on a file with its weight (reward)
        #store
        self.save_choice()

        return choice
    
    def seq3(self):
        #reward him for making a sequence of 3
        self.reward +=100

    def wins(self):
        #if the last move wins the game reward him
        self.reward += 100000
        self.no_games += 1

    def loses(self):
        #if he loses reward him negatively
        self.reward -= 10000
    
    def save_choice(self, file):
        #store its choice on a file with its weight (reward)
        #store

        return
    
    def reset(self):
        self.reward=0
