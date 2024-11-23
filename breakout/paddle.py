class Paddle:
    def __init__(self, x=50, y=20, width=10):
        self.x = x
        self.y = y
        self.width = width

    def move(self, direction):
        if direction == "esq":
            self.x -= 1
        elif direction == "dir":
            self.x += 1
        print(f"A raquete se moveu para a {direction}. Nova posição: x={self.x}, y={self.y}")