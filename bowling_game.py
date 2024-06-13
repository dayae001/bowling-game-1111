class BowlingGame:
    def __init__(self):
        self.score_board = []

    def roll(self, pins):
        if pins == 10:
            self.score_board.append(pins)
            self.score_board.append(0)
        else:
            self.score_board.append(pins)

    def score(self):
        rst = sum(self.score_board)

        for i in range(len(self.score_board) // 2 - 1):
            if (self.score_board[i * 2] != 10 and self.score_board[i * 2 + 1] != 10) and (
                    self.score_board[i * 2] + self.score_board[i * 2 + 1] == 10):
                rst += self.score_board[(i + 1) * 2]

            if (self.score_board[i * 2] == 10 or self.score_board[i * 2 + 1] == 10):
                if i >= 9:
                    continue
                if self.score_board[(i + 1) * 2] != 10:
                    rst += self.score_board[(i + 1) * 2]
                    rst += self.score_board[(i + 1) * 2 + 1]
                else:
                    rst += self.score_board[(i + 1) * 2]
                    rst += self.score_board[(i + 2) * 2]

        return rst
