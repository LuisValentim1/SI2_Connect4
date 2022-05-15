class Move:
    def __init__(self, board_state, reward, choice):
        self.board_state = board_state
        self.reward = reward
        self.sum_board = self.calc_sum_board(self.board_state)
        self.choice = choice

    @staticmethod
    def calc_sum_board(board_state):
        board_total = 0
        for position in board_state:
            board_total += position.fill
        return board_total

    def __str__(self):
        return f"Move {self.reward},{self.sum_board},{self.choice}"

    def __repr__(self):
        return f"Move {self.reward},{self.sum_board},{self.choice}"