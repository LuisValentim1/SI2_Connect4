from os import system
from board import Board
from move import Move
import copy 


class oslaAgent:

    def __init__(self, player_num):
        self.name = "osla Agent"
        self.no_seq3 = 0
        self.player_num = player_num
        self.simBoard = Board()
        

    def play(self, board, move_dict):
        
        return self.getBestMove(board)

    def getBestMove(self, board):
        moveValues = []
        for move in range(0,7):
            value = self.evalBoard(board, move, self.player_num)
            moveValues.append(value)

        bestMoveVal = 0
        bestMove = 0
        for val in moveValues:
            if val > bestMoveVal:
                bestMoveVal = val 
                bestMove = moveValues.index(val)

        return bestMove

    def evalBoard(self, board : Board, move, player):
        self.simBoard.copy_stats(board.positions, board.sequences)
        #self.simBoard = copy.deepcopy(board)

        self.simBoard.placePiece(move, self.player_num)
        self.simBoard.checkWinner()

        if self.simBoard.winner == player:
            return 10000

        if self.blockedSeq3(board, (3%player)+1, move):
            return 1000

        if self.madeSeq3(board, self.simBoard, player):
            return 100

        if self.madeSeq(board, self.simBoard, player):
            return 10 

        return 1

    def blockedSeq3(self, board, opPlayer, move):
        simBoard = copy.deepcopy(board)
        simBoard.placePiece(move, self.player_num)
        simBoard.checkWinner()
        if(simBoard.winner == opPlayer):
            return True

    def madeSeq3(self, board, simulatedBoard, player):
        if(len(board.getSequencesFromPlayerWithLength( 3, player)) < 
        len(simulatedBoard.getSequencesFromPlayerWithLength( 3, player))):
            return True

    def madeSeq(self, board, simulatedBoard, player):
        if(len(simulatedBoard.getSequencesFromPlayer(player))-len(board.getSequencesFromPlayer(player)) == 2 ):
            return True

    def print_board(self,board):
        [print(b.fill,end=",") for b in board]