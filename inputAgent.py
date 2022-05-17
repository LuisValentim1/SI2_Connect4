from os import system
from board import Board
from move import Move
import copy 


class inputAgent:

    def __init__(self, player_num):
        self.name = "User Input"   

    def play(self):
        x = input()
        return x
