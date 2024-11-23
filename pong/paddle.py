from pong.position import Position

class Paddle:
    def __init__(self, position: Position, width: int, height: int, speed: int):
        self.position = position
        self.width = width
        self.height = height
        self.speed = speed

    def move_up(self):
        if self.position.y > 0:  # if paddle can move up
            self.position.y -= self.speed
        print(f"Raquete movida para cima. Nova posição: {self.position.y}")

    def move_down(self, field_height: int):
        if self.position.y + self.height < field_height:  # if paddle can move down
            self.position.y += self.speed
        print(f"Raquete movida para baixo. Nova posição: {self.position.y}")