from numpy import true_divide


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fill = 0

    def placePiece(self, player):
        self.fill = player

    def inSequence(self, pos, dir):
        if pos.fill == self.fill:
            if pos.x == self.x and pos.y == self.y+1 and dir!="horizontal" and dir!="perp+" and dir!="perp-":
                return True
            if pos.y == self.y and pos.x == self.x+1 and dir!="vertical" and dir!="perp+" and dir!="perp-":
                return True
            if pos.x == self.x+1 and pos.y == self.y+1 and dir!="horizontal" and dir!="vertical" and dir!="perp-":
                return True
            if pos.x == self.x-1 and pos.y == self.y+1 and dir!="horizontal" and dir!="perp+" and dir!="vertical":
                return True
        return False

    def inReverseSequence(self, pos, dir):
        if pos.fill == self.fill :
            if pos.y == self.y and pos.x == self.x-1 and dir!="vertical" and dir!="perp+" and dir!="perp-":
                return True
            if pos.x == self.x-1 and pos.y == self.y-1 and dir!="horizontal" and dir!="vertical" and dir!="perp-":
                return True
            if pos.x == self.x+1 and pos.y == self.y-1 and dir!="horizontal" and dir!="perp+" and dir!="vertical":
                return True
        return False