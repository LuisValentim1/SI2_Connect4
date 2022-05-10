from position import Position 
from sequence import Sequence 
import pygame

class Board:

    positions = []
    sequences = []

    def __init__(self):   
        y = 0
        while y < 6:
            x = 0
            while x < 7:
                self.positions.append(Position(x,y))
                x = x+1
            y = y+1

    def placePiece(self, x, player):
        for pos in self.positions:
            if(pos.x == x and pos.fill == 0):
                pos.placePiece(player)
                return 1
        print("This column is full")
        return 0

    def show(self, screen):
        for pos in self.positions:
            if pos.fill == 0:  
                pygame.draw.circle(screen, (255, 255, 255), (70*pos.x + 40, 465-70*pos.y), 30)
            if pos.fill == 1:  
                pygame.draw.circle(screen, (255, 0, 0), (70*pos.x + 40, 465-70*pos.y), 30)
            if pos.fill == 2:  
                pygame.draw.circle(screen, (255, 255, 0), (70*pos.x + 40, 465-70*pos.y), 30)
        return 0

    def reset(self):
        for pos in self.positions:
            pos.fill = 0
        self.winner = ""
        self.sequences = []

    def gameState(self):
        curSequences = []
        for pos in self.positions:
            if pos.fill != 0:
                curSequences.append(Sequence(pos))
                for seq in curSequences:
                    inSequenceFlag = seq.allows(pos)
                    if inSequenceFlag == 1:
                        seq.addPieceAtTheEnd(pos)
                    if inSequenceFlag == 2:
                        seq.addPieceAtTheStart(pos)
        self.sequences = curSequences

    def checkWinner(self):
        for seq in self.sequences:
            if seq.length == 4:
                self.winner = seq.player
                print("Player" + str(self.winner) + " wins!! ")
                self.reset()
                return True

