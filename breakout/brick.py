
class Brick:
    def __init__(self, x, y, width=3):
        self.x = x
        self.y = y
        self.width = width
        self.destroyed = False

    def __repr__(self):
        return f"Bloco(x={self.x}, y={self.y}, destruído={self.destroyed})"
