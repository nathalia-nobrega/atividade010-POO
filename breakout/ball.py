class Ball:
    def __init__(self, x=5, y=5, dx=1, dy=1):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy

    def move(self):
        self.x += self.dx
        self.y += self.dy
        print(f"A bola se moveu. Nova posição: x={self.x}, y={self.y}")

    def detect_collision(self, paddle, bricks, walls):
        # Collision with walls
        if self.x <= 0 or self.x >= walls["width"]:
            self.dx *= -1
            print("A bola colidiu com a parede de blocos..")

        if self.y <= 0:
            self.dy *= -1
            print("A bola colidiu com o teto.")

        # Collision with paddle
        if self.y == paddle.y and paddle.x <= self.x <= paddle.x + paddle.width:
            self.dy *= -1
            print("A bola colidiu com a raquete.")

        # Collision with bricks
        for brick in bricks:
            if not brick.destroyed and brick.x <= self.x <= brick.x + brick.width and brick.y == self.y:
                brick.destroyed = True
                self.dy *= -1
                print(f"A bola colidiu com um bloco em x={brick.x}, y={brick.y}. O bloco foi destruído.")
                return True

        return False

