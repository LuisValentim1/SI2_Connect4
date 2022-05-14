import random

class RLAgent:

    def __init__(self):
        self.name = "RL Agent"
        self.reward = 0
        self.no_games = 0
        self.no_seq3 = 0

    def play(self):
        #define rewards for each play

        #reward him for playing
        self.reward += 1 

        #read
        choice= None

        random_no_games = 100000 #change later
        if self.no_games<random_no_games:
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
    
    def seq3(self, no_seq3):
        #reward him for making a sequence of 3
        if no_seq3 > self.no_seq3:
            nseq3 = no_seq3 - self.no_seq3
            self.no_seq3 = no_seq3

            self.reward += 100*nseq3

    def wins(self, sequences):
        #if the last move wins the game reward him
        self.reward += 100000
        self.no_games += 1
        self.reset()

    def loses(self):
        #if he loses reward him negatively
        self.reward -= 10000
    
    def save_choice(self, sequences, file):
        #store its choice on a file with its weight (reward)
        #store

        return
    
    def check_sequences(self, sequences):
        return
    
    def reset(self):
        self.reward=0
        self.no_seq3=0
