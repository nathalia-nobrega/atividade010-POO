from pong.position import Position

class Wall:
    def __init__(self, x: int, y: int, width: int, height: int):
        self.position = Position(x, y)
        self.width = width
        self.height = height
