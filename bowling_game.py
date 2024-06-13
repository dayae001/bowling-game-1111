class BowlingGame:
    def __init__(self):
        self.score_board = []

    def roll(self, pins):
        self.score_board.append(pins)

    def score(self):
        rst = sum(self.score_board)

        for i in range(len(self.score_board) // 2):
            if self.score_board[i * 2] + self.score_board[i * 2 + 1] == 10:
                rst += self.score_board[(i + 1) * 2]
        return rst
