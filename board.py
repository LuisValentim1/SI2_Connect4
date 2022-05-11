from position import Position 
from sequence import Sequence 
import pygame

class Board:

    positions = []

    def __init__(self):   
        y = 0
        while y < 6:
            x = 0
            while x < 7:
                self.positions.append(Position(x,y))
                x = x+1
            y = y+1
        self.winner=""
        self.sequences = []

    # set a piece in a position
    def placePiece(self, x, player):
        for pos in self.positions:
            if(pos.x == x and pos.fill == 0):
                pos.placePiece(player)
                return 7
        #print("This column is full")

    # show the board pieces in place 
    def show(self, screen):
        for pos in self.positions:
            if pos.fill == 0:  
                pygame.draw.circle(screen, (255, 255, 255), (70*pos.x + 40, 465-70*pos.y), 30)
            if pos.fill == 1:  
                pygame.draw.circle(screen, (255, 0, 0), (70*pos.x + 40, 465-70*pos.y), 30)
            if pos.fill == 2:  
                pygame.draw.circle(screen, (255, 255, 0), (70*pos.x + 40, 465-70*pos.y), 30)
        return 0

    # reset the board state, all positions go back to 0, meaning open positions
    def reset(self):
        for pos in self.positions:
            pos.fill = 0
        self.winner = ""
        self.sequences = []

    # check which sequences active and who they belong tho
    def gameState(self):

        # starts empty 
        curSequences = []

        # for every filled position 
        for pos in self.positions:
            altSequences = []
            if pos.fill != 0:

                # append that position to the curent sequences 
                curSequences.append(Sequence(pos))

                # and check if they extend any other sequence, whenever a sequence gets extended create a copy of its previous state 
                # because other sequence might be created from it, pieces making an L scenario
                for seq in curSequences:
                    inSequenceFlag = seq.allows(pos)
                    if inSequenceFlag == 1:
                        if(seq.length==1):
                            altSequences.append(Sequence(seq.startingPos))
                        seq.addPieceAtTheEnd(pos)
                    if inSequenceFlag == 2:
                        if(seq.length==1):
                            altSequences.append(Sequence(seq.startingPos))
                        seq.addPieceAtTheStart(pos)
            for aSeq in altSequences:
                curSequences.append(aSeq)
        self.sequences = curSequences

    # verify if there's any winning sequence 
    def checkWinner(self):
        self.gameState()
        for seq in self.sequences:
            if seq.length == 4:
                self.winner = seq.player
                print("Player" + str(self.winner) + " wins!! ")
                return True  

#def get_heuristic(grid, mark, config):
    #num_threes = count_windows(grid, 3, mark, config)
    #num_fours = count_windows(grid, 4, mark, config)
    #num_threes_opp = count_windows(grid, 3, mark%2+1, config)
    #num_fours_opp = count_windows(grid, 4, mark%2+1, config)
    #score = num_threes - 1e2*num_threes_opp - 1e4*num_fours_opp + 1e6*num_fours
    #return score

