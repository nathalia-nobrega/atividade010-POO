from pong.position import Position


class Brick:
    def __init__(self, position: Position, width=3):
        self.position = position
        self.width = width
        self.destroyed = False

    def __repr__(self):
        return f"Bloco(x={self.position.x}, y={self.position.y}, destruído={self.destroyed})"
