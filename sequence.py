from position import Position 

class Sequence:
  def __init__(self, pos):
      self.startingPos = pos
      self.finalPos = pos
      self.length = 1
      self.direction = "single"
      self.player = pos.fill

  # Add piece to the end of the sequence if the sequence was previously a single set the direction
  def addPieceAtTheEnd(self, pos):
    if self.length < 2:
      if(pos.x == self.startingPos.x):
        self.direction = "vertical"
      if(pos.y == self.startingPos.y):
        self.direction = "horizontal"
      if(pos.y == self.finalPos.y+1 and pos.x == self.finalPos.x+1):
        self.direction = "perp+"
      if(pos.y == self.finalPos.y+1 and pos.x == self.finalPos.x-1):
        self.direction = "perp-"
    self.finalPos = pos
    self.length = self.length+1

  # Add piece to the start of a sequence if the sequence was previously a single set the direction
  def addPieceAtTheStart(self,pos):
    if self.length < 2:
      if(pos.y == self.startingPos.y):
        self.direction = "horizontal"
      if(pos.y == self.startingPos.y-1 and pos.x == self.startingPos.x+1):
        self.direction = "perp-"
      if(pos.y == self.startingPos.y-1 and pos.x == self.startingPos.x-1):
        self.direction = "perp+"
    self.startingPos = pos
    self.length = self.length+1

  # Check if two positions are in sequence
  def allows(self, pos):
    if self.finalPos.inSequence(pos, self.direction):
      return 1
    if self.startingPos.inReverseSequence(pos, self.direction):
      return 2
    return 0

  def print(self):
    return self.startingPos.print() + " - " + self.finalPos.print()

      