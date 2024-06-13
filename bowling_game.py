class BowlingGame:
    score_board = []
    def roll(self, pins):
        self.score_board.append(pins)

    def score(self):
        return sum(self.score_board)