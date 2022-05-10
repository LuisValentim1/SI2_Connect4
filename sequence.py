from position import Position 

class Sequence:
  def __init__(self, pos):
      self.startingPos = pos
      self.finalPos = pos
      self.length = 1
      self.direction = ""
      self.player = pos.fill

  def addPieceAtTheEnd(self, pos):
    if self.length < 2:
      if(pos.x == self.startingPos.x):
        self.direction = "vertical"
      if(pos.y == self.startingPos.y):
        self.direction = "horizontal"
      if(pos.y == self.startingPos.y+1 and pos.x == self.startingPos.x+1):
        self.direction = "perp+"
      if(pos.y == self.startingPos.y+1 and pos.x == self.startingPos.x-1):
        self.direction = "perp-"
    self.finalPos = pos
    self.length = self.length+1

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

  def allows(self, pos):
    if self.finalPos.inSequence(pos, self.direction):
      return 1
    if self.startingPos.inReverseSequence(pos, self.direction):
      return 2
    return 0

      