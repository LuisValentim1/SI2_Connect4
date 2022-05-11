import random 

class RandomAgent:

  def __init__(self):
      self.name = "Random Agent"

  def play(self):
    return random.randint(0, 6)

    