from sequence import Sequence
from board import Board 
from position import Position 
import pygame

#Runs custom number of matches(numOfMatches) between 2 agents(agent1 and agent2) automatically 
class Simulator:
    def __init__(self, agent1, agent2, numOfMatches, gameBoard : Board):
      self.agent1 = agent1
      self.agent2 = agent2
      self.numOfMatches = numOfMatches
      self.gameBoard = gameBoard
      self.matchesPlayed = 0
      self.a1Wins = 0
      self.a2Wins = 0
      self.numOfDraws = 0
      self.drawPercentage = 0
      self.a1WinPercentage = 0
      self.a2WinPercentage = 0

    # Calculating win percentage of each AI 
    def calcWinRates(self):
        self.a1WinPercentage = (self.a1Wins/self.matchesPlayed) * 100
        self.a2WinPercentage = (self.a2Wins/self.matchesPlayed) * 100

    # Printing function with results of a given simulation
    def show(self):
        print("Number of Matches Player : " + str(self.matchesPlayed))
        print("............................................")
        print("Agent 1 : " + self.agent1.name)
        print("Number of Agent 1 Wins : " + str(self.a1Wins))
        print("Agent 1 Win Percentage : " + str(self.a1WinPercentage) + "%")
        print("............................................")
        print("Agent 2 : " + self.agent2.name)
        print("Number of Agent 2 Wins : " + str(self.a2Wins))
        print("Agent 2 Win Percentage : " + str(self.a2WinPercentage) + "%")
        print("______________________________________________")
    
    # Refresh image so we can see the AI playing in real time
    def refresh(self, screen):
        screen.fill((50, 50, 255))
        self.gameBoard.show(screen)
        pygame.display.flip()
        pygame.time.wait(200)

    # Check who won and register data accordingly 
    def checkWinner(self):
        choice = self.gameBoard.checkWinner()
        if(self.gameBoard.winner == 1):
            self.a1Wins += 1 
        if(self.gameBoard.winner == 2):
            self.a2Wins += 1
        if(self.gameBoard.winner == "draw"):
            self.numOfDraws += 1 
        return choice

    # Method which runs the simulation 
    def run(self, screen):

        # Run for as long as the matches played is inferior the the total number of matches 
        while self.matchesPlayed < self.numOfMatches:

            # Run a match for as long as the winner is not decided 
            while self.gameBoard.winner == "":

                # Each agent takes turns making a move, the system verifies if someone won and refreshes the board after every move
                # 0 is the return on an invalid play, so if a player makes an invalid move 
                # such as trying to play in a filled column or a non valid input the system will ask for a new play
                move = self.gameBoard.placePiece(self.agent1.play(), 1)
                if move == 0:
                    self.gameBoard.winner = 2
                    if self.agent1.name == "RL Agent":    
                        self.agent1.loses(self.gameBoard.positions)
                
                #check for sequences of 3
                if(self.agent1.name == "RL Agent"):
                    self.agent1.seq3(self.gameBoard.getSequencesFromPlayerWithLength(3, 1).__len__())

                self.refresh(screen)
                a1_win = self.checkWinner()
                #self.printSequences()
                if a1_win == 1 and self.agent1.name == "RL Agent":
                    self.agent1.wins(self.gameBoard.positions)

                if a1_win == 1 and self.agent2.name == "RL Agent":
                    self.agent2.loses(self.gameBoard.positions)

                #if there is no winner its player 2's turn
                if self.gameBoard.winner == "":
                    move = self.gameBoard.placePiece(self.agent2.play(), 2)
                    if move == 0:
                        self.gameBoard.winner = 1
                        if self.agent2.name == "RL Agent":    
                            self.agent2.loses(self.gameBoard.positions)

                    #check for sequences of 3
                    if self.agent2.name == "RL Agent":
                        self.agent2.seq3(self.gameBoard.getSequencesFromPlayerWithLength(3, 2).__len__())

                    #self.printSequences()
                    self.refresh(screen)
                    a2_win = self.checkWinner()
                    
                    if a2_win == 1 and self.agent2.name == "RL Agent":
                        self.agent2.wins(self.gameBoard.positions)
                        
                    if a2_win == 1 and self.agent1.name == "RL Agent":
                        self.agent1.loses(self.gameBoard.positions)
                    
            # After a match is over and a winner is decided we increment the matches count and reset the board         
            self.matchesPlayed += 1
            pygame.time.wait(1000)
            self.gameBoard.reset()

        #After every match has been played, calculate statistics and show results 
        self.calcWinRates()
        self.show()
        return False

    #Debug tool
    def printSequences(self):
        for seq in self.gameBoard.sequences:
            print(seq.print())
        "..................................."