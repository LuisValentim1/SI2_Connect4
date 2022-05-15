import random 

class RandomAgent:

  def __init__(self):
      self.name = "Random Agent"

  def play(self, board):
    return random.randint(0, 6)

    