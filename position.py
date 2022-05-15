from numpy import true_divide


class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.fill = 0

    def placePiece(self, player):
        self.fill = player

    # Check if the position being tested is directly above, to the right, right top diagonal 
    # or left top diagonal of this piece if that's the case they're in sequence return true
    def inSequence(self, pos, dir):
        if pos.fill == self.fill:
            if pos.x == self.x and pos.y == self.y+1 and (dir=="vertical" or dir=="single"):
                return True
            if pos.y == self.y and pos.x == self.x+1 and (dir=="horizontal" or dir=="single"):
                return True
            if pos.x == self.x+1 and pos.y == self.y+1 and (dir=="perp+" or dir=="single"):
                return True
            if pos.x == self.x-1 and pos.y == self.y+1 and (dir=="perp-" or dir=="single"):
                return True
        return False

    # Check if the position being tested is directly to the left, left down diagonal or 
    # right down diagonal of this piece if that's the case they're in sequence, return true
    def inReverseSequence(self, pos, dir):
        if pos.fill == self.fill :
            if pos.y == self.y and pos.x == self.x-1 and (dir=="horizontal" or dir=="single"):
                return True
            if pos.x == self.x-1 and pos.y == self.y-1 and (dir=="perp+" or dir=="single"):
                return True
            if pos.x == self.x+1 and pos.y == self.y-1 and (dir=="perp-" or dir=="single"):
                return True
        return False

    def print(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.fill == other.fill

    def copy(self):
        p = Position(self.x, self.y)
        p.fill = self.fill
        return p
