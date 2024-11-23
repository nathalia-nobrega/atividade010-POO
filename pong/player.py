class Player:
    def __init__(self, score, paddle):
        self.score = score
        self.paddle = paddle

    def increase_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_paddle(self):
        return self.paddle

    def move_paddle_up(self):
        self.paddle.move_up()

    def move_paddle_down(self, field_height: int):
        self.paddle.move_down(field_height)
