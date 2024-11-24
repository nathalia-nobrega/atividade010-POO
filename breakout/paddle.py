from pong.position import Position


class Paddle:
    def __init__(self, position: Position, width=10):
        self.position = position
        self.width = width

    def move(self, direction):
        if direction == "esq":
            self.position.x -= 1
        elif direction == "dir":
            self.position.y += 1
        print(f"A raquete se moveu para a {direction}. Nova posição: x={self.position.x}, y={self.position.y}")